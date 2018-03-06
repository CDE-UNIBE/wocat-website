from classytags.helpers import InclusionTag
from django import template
from django.conf import settings

register = template.Library()


@register.tag
class Piwik(InclusionTag):
    name = 'piwik'
    template = 'piwik/widget.html'

    def get_context(self, context, **kwargs):
        return {
            'domain': 'wocat.net',
            'site_id': settings.PIWIK_SITE_ID,
            'user_id': self.get_user_id(context)
        }

    def get_user_id(self, context):
        if hasattr(context, 'request') and hasattr(context.request, 'user') and context.request.user.is_authenticated:
            return context.request.user.id
        return ''
