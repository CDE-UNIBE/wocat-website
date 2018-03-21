from django.conf import settings


def template_settings(request):
    """
    Put selected setting variables to the template
    """
    setting_values = [
        'GOOGLE_WEBMASTER_TOOLS_KEY',
        'FEATURE_SHOW_TRANSLATIONS',
    ]
    return {value: getattr(settings, value) for value in setting_values}
