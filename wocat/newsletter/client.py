import logging

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from mailchimp3 import MailChimp
from mailchimp3.helpers import get_subscriber_hash
import requests

from wocat.users.models import User

logger = logging.getLogger('mailchimp_client')


class NewsletterClient:
    """
    Wrapper around the mailchimp client.
    """
    list_id = settings.NEWSLETTER_LIST_ID
    # http://developer.mailchimp.com/documentation/mailchimp/reference/lists/members/#edit-put_lists_list_id_members_subscriber_hash
    # subscribed, unsubscribed, cleaned, pending, transactional
    default_new_status = 'subscribed'

    @property
    def client(self):
        """
        Get the MailChimp client 
        """
        return MailChimp(
            mc_user=settings.NEWSLETTER_USERNAME,
            mc_secret=settings.NEWSLETTER_API_KEY,
            request_headers=self.headers
        )

    @property
    def headers(self):
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

    def update_member(self, user: User) -> None:
        """
        Update a single users data. 
        """
        response = self.client.lists.members.create_or_update(
            list_id=self.list_id,
            subscriber_hash=get_subscriber_hash(member_email=user.email),
            data={
                'email_address': user.email,
                'status': self.get_status(user=user),
                'status_if_new': self.default_new_status,
                'merge_fields': {
                    'FNAME': user.first_name,
                    'LNAME': user.last_name,
                }
            }
        )
        logger.info(response)

newsletter_client = NewsletterClient()
