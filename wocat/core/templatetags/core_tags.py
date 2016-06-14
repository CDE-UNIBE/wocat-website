from classytags.helpers import InclusionTag
from django import template
from django.core.urlresolvers import reverse
from menus.templatetags.menu_tags import ShowMenu, ShowBreadcrumb

register = template.Library()


@register.tag
class Header(InclusionTag):
    name = 'header'
    template = 'widgets/header.html'

    def get_context(self, context, **kwargs):
        nodes = ShowMenu.get_context(self, context, 1, 100, 100, 100, 'widgets/menu.html', None, None, None).get('children')
        user = context.get('user')
        if user.is_authenticated():
            user_link = {'url': reverse('users:detail', args=[user.username]), 'text': user.username}
        else:
            user_link = {'url': reverse('account_login'), 'text': 'Login'}
        return {
            'id': '1',
            'toplinks': [
                {'url': '#facebook', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>'},
                {'url': '#youtube', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>'},
                {'url': '#twitter', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>'},
                {'url': '#get-involved', 'text': 'Get involved'},
                {'url': '#faq', 'text': 'FAQ'},
                {'url': '#glassary', 'text': 'Glossary'},
                user_link,
                {
                    'dropdown': True,
                    'text': 'EN',
                    'links': [
                        {'url': '#de', 'text': 'DE', 'active': True,},
                        {'url': '#fr', 'text': 'FR'},
                    ]
                },
                {'url': '#search', 'text': '<i class="fa fa-search" aria-hidden="true"></i>'},
            ],
            'mainnav': {
                'depth': 1,
                # only visible if in or under a project page
                'brand2': {
                    'src': '/static/styleguide/test-images/dog-1by1.jpg',
                    'name': 'Projekt',
                    'href': '#project-page',
                },
                'links1': [{'url': node.get_absolute_url, 'text': node.title} for node in nodes],
                'links2': [{'url': node.get_absolute_url, 'text': node.title} for node in nodes],
            },
        }


@register.tag
class Breadcrumb(InclusionTag):
    name = 'breadcrumb'
    template = 'widgets/breadcrumb.html'

    def get_context(self, context, **kwargs):
        nodes = ShowBreadcrumb.get_context(self, context, 0, None, True).get('ancestors')
        return {
            'links': [{'href': node.get_absolute_url if not node.selected else None, 'text': node.title} for node in nodes],
        }
