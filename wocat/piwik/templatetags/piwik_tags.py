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
            'user_id': context.request.user.id if context.request.user.is_authenticated else ''
        }
