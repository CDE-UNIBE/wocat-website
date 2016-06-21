from classytags.helpers import InclusionTag
from django import template
from django.core.urlresolvers import reverse

from wocat.cms.models import HomePage

register = template.Library()


@register.tag
class Header(InclusionTag):
    name = 'header'
    template = 'widgets/header.html'

    def get_node(self, page, current_page, ancestors):
        return {
            'text': page.title,
            'url': page.url,
            # Checking if this page is in the tree of active pages
            'active': page == current_page or page in ancestors,
        }

    def get_nodes(self, context):
        current_page = context.get('page')
        home_page = HomePage.objects.live().in_menu().first()
        main_pages = home_page.get_children().live().in_menu().specific()
        if current_page:
            current_page = current_page.specific
            ancestors = current_page.get_ancestors().live().in_menu().specific()
        else:
            ancestors = []
        return [self.get_node(page, current_page=current_page, ancestors=ancestors) for page in main_pages]

    def get_context(self, context, **kwargs):
        nodes = self.get_nodes(context)
        # nodes = []
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
                'links1': nodes,
                'links2': nodes,
            },
        }


@register.tag
class Breadcrumb(InclusionTag):
    name = 'breadcrumb'
    template = 'widgets/breadcrumb.html'

    def get_node(self, page, current_page, ancestors):
        return {
            'text': page.title,
            'href': page.url if not page == current_page else None,
        }

    def get_nodes(self, context):
        current_page = context.get('page')
        if current_page:
            current_page = current_page.specific
            ancestors = current_page.get_ancestors().live().in_menu().specific()
        else:
            ancestors = []
        return [self.get_node(page, current_page=current_page, ancestors=ancestors) for page in ancestors] + [
            self.get_node(current_page, current_page=current_page, ancestors=ancestors)]

    def get_context(self, context, **kwargs):
        nodes = self.get_nodes(context)
        return {'links': nodes}
