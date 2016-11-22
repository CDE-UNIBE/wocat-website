import mailchimp
from django.conf import settings

API_KEY = settings.NEWSLETTER_API_KEY
LIST_ID = settings.NEWSLETTER_LIST_ID


def get_api():
    if API_KEY and LIST_ID:
        return mailchimp.Mailchimp(API_KEY)


def subscribe_to_newsletter(user):
    api = get_api()
    if api and user:
        api.lists.subscribe(LIST_ID, {'email': user.email}, update_existing=True)
        return True
    else:
        return False


def unsubscribe_from_newsletter(user):
    api = get_api()
    if api and user:
        api.lists.unsubscribe(LIST_ID, {'email': user.email})
        return True
    else:
        return False
