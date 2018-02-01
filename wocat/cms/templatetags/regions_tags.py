from classytags.helpers import InclusionTag
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.tag
class Region(InclusionTag):
    name = 'region'
    template = 'widgets/teaser.html'

    def get_context(self, context, **kwargs):
        region = context.get('region')
        if region:
            region = region.specific
            return {
                'description': '',
                # 'flag_iso_3166_1_alpha_3': '',
                'href': region.url,
                'map': {'countries': [{'iso_3166_1_alpha_3': country.code} for country in region.countries], 'size': 'small'},
                'readmorelink': {'text': _('To the region')},
                'title': region,
            }
        else:
            return {}
