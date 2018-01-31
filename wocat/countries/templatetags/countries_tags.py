from classytags.helpers import InclusionTag
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.tag
class Country(InclusionTag):
    name = 'country'
    template = 'widgets/teaser.html'

    def get_context(self, context, **kwargs):
        country = context.get('country')
        if country:
            country = country.specific
            return {
                'description': '',
                'flag_iso_3166_1_alpha_3': country.code,
                'href': country.url,
                'map': {'countries': [{'iso_3166_1_alpha_3': country.code}], 'size': 'small'},
                'readmorelink': {'text': _('To the country')},
                'title': country,
            }
        else:
            return {}
