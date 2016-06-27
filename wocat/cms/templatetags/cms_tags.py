from classytags.arguments import Argument
from classytags.core import Options
from classytags.helpers import InclusionTag
from django import template
from django.core.urlresolvers import reverse
from django.utils.html import format_html

from wocat.cms.models import HomePage, ProjectPage, ProjectsPage

register = template.Library()


@register.tag
class Header(InclusionTag):
    name = 'header'
    template = 'widgets/header.html'

    def get_node(self, page, current_page, ancestors):
        text = page.title
        if hasattr(page, 'flag'):
            text = format_html('<strong>flag</strong>{}', text)
        return {
            'text': text,
            'href': page.url,
            # Checking if this page is in the tree of active pages
            'active': page == current_page or page in ancestors,
        }

    def get_nodes(self, context, root_page=None):
        current_page = context.get('page')
        if not root_page:
            root_page = HomePage.objects.live().in_menu().first()
        if not root_page:
            return []
        main_pages = root_page.get_children().live().in_menu().specific()
        if current_page:
            current_page = current_page.specific
            ancestors = current_page.get_ancestors().live().in_menu().specific()
        else:
            ancestors = []
        return [self.get_node(page, current_page=current_page, ancestors=ancestors) for page in main_pages]

    def get_project_page(self, page):
        if isinstance(page, ProjectPage):
            return page
        project_page = page.get_ancestors().type(ProjectPage).first()
        if project_page:
            return project_page

    def get_context(self, context, **kwargs):
        page = context.get('page')
        project_page = self.get_project_page(page)
        nodes = self.get_nodes(context, root_page=project_page)
        user = context.get('user')
        if user.is_authenticated():
            user_link = {'href': reverse('users:detail', args=[user.username]), 'text': user.username}
        else:
            user_link = {'href': reverse('account_login'), 'text': 'Login'}
        if project_page:
            depth = 2
            brand2 = {
                'src': '/static/styleguide/test-images/dog-1by1.jpg',
                'name': project_page.title,
                'href': project_page.url,
            }
        else:
            depth = 1
            brand2 = {}
        return {
            'id': '1',
            'toplinks': [
                {'href': '#facebook', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>'},
                {'href': '#youtube', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>'},
                {'href': '#twitter', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>'},
                {'href': '#get-involved', 'text': 'Get involved'},
                {'href': '#faq', 'text': 'FAQ'},
                {'href': '#glassary', 'text': 'Glossary'},
                user_link,
                {
                    'dropdown': True,
                    'text': 'EN',
                    'links': [
                        {'href': '#de', 'text': 'DE', 'active': True,},
                        {'href': '#fr', 'text': 'FR'},
                    ]
                },
                {'href': '#search', 'text': '<i class="fa fa-search" aria-hidden="true"></i>'},
            ],
            'mainnav': {
                'depth': depth,
                # only visible if in or under a project page
                'brand2': brand2,
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
            return [self.get_node(page, current_page=current_page, ancestors=ancestors) for page in ancestors] + [
                self.get_node(current_page, current_page=current_page, ancestors=ancestors)]
        else:
            return []

    def get_context(self, context, **kwargs):
        nodes = self.get_nodes(context)
        return {'links': nodes}


@register.tag
class Carousel(InclusionTag):
    name = 'carousel'
    template = 'widgets/carousel.html'
    options = Options(
        Argument('images', required=True),
    )

    def get_context(self, context, images, **kwargs):
        items = []
        for image in images:
            items.append({'src': image.value.get_rendition('max-1200x1200').url})
        return {'items': items}
