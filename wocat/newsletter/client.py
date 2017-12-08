import logging
import functools

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models.signals import post_save
from mailchimp3 import MailChimp
from mailchimp3.helpers import get_subscriber_hash
import requests

from wocat.users.models import User

logger = logging.getLogger('mailchimp_client')


def active_sync_only(func):
    """
    Wrapper to only execute calls to the API only if syncing is allowed.
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if settings.NEWSLETTER_IS_ACTIVE_SYNC:
            func(self, *args, **kwargs)
    return wrapper


class NewsletterClient:
    """
    Wrapper around the mailchimp client.
    """
    list_id = settings.NEWSLETTER_LIST_ID

    @property
    def client(self) -> MailChimp:
        """
        Get the MailChimp client 
        """
        return MailChimp(
            mc_user=settings.NEWSLETTER_USERNAME,
            mc_secret=settings.NEWSLETTER_API_KEY,
            request_headers=self.headers
        )

    @property
    def headers(self) -> requests.structures.CaseInsensitiveDict:
        """
        MailChimp recommends to add a User-Agent. 
        """
        headers = requests.utils.default_headers()
        headers['User-Agent'] = 'Wocat Website (wocat@wocat.net)'
        return headers

    def get_status(self, user: User) -> str:
        is_subscribed = user.is_active and user.newsletter
        try:
            validate_email(user.email)
            has_valid_email = True
        except ValidationError:
            has_valid_email = False
        return 'subscribed' if is_subscribed and has_valid_email else 'unsubscribed'

    @active_sync_only
    def update_member(self, user: User) -> None:
        """
        Update a single users data. 
        """
        subscription_status = self.get_status(user=user)
        try:
            response = self.client.lists.members.create_or_update(
                list_id=self.list_id,
                subscriber_hash=get_subscriber_hash(member_email=user.email),
                data={
                    'email_address': user.email,
                    'status': subscription_status,
                    'status_if_new': subscription_status,
                    'merge_fields': {
                        'FNAME': user.first_name,
                        'LNAME': user.last_name,
                    }
                }
            )
            logger.info(response)

        except requests.HTTPError:
            # This usually means that the person has unsubscribed via MailChimp.
            # If this is the case, unsubscribe the user - and don't submit this
            # to the API via signal!
            if not self.is_active_member(user=user):
                from .signals import update_newsletter_subscription
                post_save.disconnect(update_newsletter_subscription, sender=User)
                user.unsubscribe()
                post_save.connect(update_newsletter_subscription, sender=User)


    @active_sync_only
    def is_active_member(self, user: User) -> bool:
        try:
            response = self.client.lists.members.get(
                list_id=self.list_id,
                subscriber_hash=get_subscriber_hash(member_email=user.email)
            )
        except requests.HTTPError:
            # Invalid request -> the user doesn't exist on MailChimp and
            # therefore is not subscribed.
            return False
        return response.get('status', '') == 'subscribed'

    @active_sync_only
    def update_all(self) -> None:
        """
        Iterate over all users and update them. 
        """
        users = User.objects.all()
        for user in users.iterator():
            self.update_member(user=user)


newsletter_client = NewsletterClient()
