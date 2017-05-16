from django.conf import settings


def webmaster_tools_key(request):
    """
    Returns a lazy 'messages' context variable.
    """
    return {
        'GOOGLE_WEBMASTER_TOOLS_KEY': settings.GOOGLE_WEBMASTER_TOOLS_KEY
    }
