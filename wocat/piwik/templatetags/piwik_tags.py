from classytags.helpers import InclusionTag
from django import template

register = template.Library()


@register.tag
class Piwik(InclusionTag):
    name = 'piwik'
    template = 'piwik/widget.html'

    def get_context(self, context, **kwargs):
        return {
            'domain': 'wocat.net',
            'site_id': 7,
            'user_id': self.get_user_id(context)
        }

    def get_user_id(self, context):
        if hasattr(context, 'request') and context.request.user.is_authenticated:
            return context.request.user.id
        return ''
