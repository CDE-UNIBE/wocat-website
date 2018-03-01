from classytags.helpers import InclusionTag
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.tag
class Project(InclusionTag):
    name = 'project'
    template = 'widgets/teaser.html'

    def get_context(self, context, **kwargs):
        project = context.get('project')
        if project:
            project = project.specific
            countries = project.countries
            map_countries = []
            for country in countries:
                map_countries.append({
                    'iso_3166_1_alpha_3': country.code,
                    'popup': '<a href="{url}">{title}</a>'.format(url=country.url, title=country)
                })
            return {
                'description': '',
                'href': project.url,
                'map': {'countries': map_countries},
                'readmorelink': {'text': _('To the project')},
                'title': project,
            }
        else:
            return {}
