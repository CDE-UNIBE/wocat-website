from classytags.helpers import InclusionTag
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _, get_language
from wagtail.wagtailcore.templatetags.wagtailcore_tags import slugurl

from wocat.cms.models import HomePage, ProjectPage

register = template.Library()


def get_profile_links(user, onlyxs=False):
    if user and user.is_authenticated():
        profile_links = {
            'dropdown': True,
            'text': user.first_name or user.email,
            'links': [
                {'href': reverse('users:detail', args=[user.email]), 'text': _('Profile'), 'active': True},
                {'href': reverse('account_logout'), 'text': _('Logout')},
            ],
            'href': reverse('users:detail', args=[user.email]),
            'onlyxs': onlyxs,
        }
    else:
        profile_links = {'href': reverse('account_login'), 'text': 'Login'}
    return profile_links


def get_social_links(onlyxs=False):
    return [
        {'href': 'https://www.facebook.com/wocatnet',
         'text': '<i class="fa fa-lg fa-facebook" aria-hidden="true"></i>', 'onlyxs': onlyxs},
        {'href': 'https://vimeo.com/user12138600', 'text': '<i class="fa fa-lg fa-vimeo" aria-hidden="true"></i>', 'onlyxs': onlyxs},
        {'href': 'https://www.youtube.com/user/WOCATEER1',
         'text': '<i class="fa fa-lg fa-youtube" aria-hidden="true"></i>', 'onlyxs': onlyxs},
        # TODO: Issue: https://github.com/FortAwesome/Font-Awesome/issues/1993 => workaround 'fa-book'
        {'href': 'https://issuu.com/wocat', 'text': '<i class="fa fa-lg fa-book" aria-hidden="true"></i>', 'onlyxs': onlyxs},
        {'href': 'http://www.slideshare.net/wocat',
         'text': '<i class="fa fa-lg fa-slideshare" aria-hidden="true"></i>', 'onlyxs': onlyxs},
    ]


def get_extra_links(context, onlyxs=False):
    return [
        {'href': slugurl(context, 'get-involved') or '#get-involved', 'text': 'Get involved', 'onlyxs': onlyxs, },
        {'href': slugurl(context, 'faq') or '#faq', 'text': 'FAQ', 'onlyxs': onlyxs, },
        {'href': reverse('glossary:list') or '#glassary', 'text': 'Glossary', 'onlyxs': onlyxs, },
    ]


@register.tag
class Header(InclusionTag):
    name = 'header'
    template = 'widgets/header.html'

    def get_lanaguage_links(self):
        current_language = get_language()
        links = []
        for code, name in settings.LANGUAGES:
            active = True if code == current_language else False
            links.append(
                {'href': reverse('switch-language', kwargs={'language': code}), 'text': name, 'active': active})
        return links

    def get_language_and_search_context(self, only_xs=True):
        return [
            # {
            #     'dropdown': True,
            #     'text': get_language(),
            #     'links': self.get_lanaguage_links(),
            #     'onlyxs': only_xs,
            # },
            {'href': reverse('search:index'), 'text': '<i class="fa fa-search" aria-hidden="true"></i>',
             'onlyxs': only_xs},
        ]

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
        if not page:
            return
        if isinstance(page, ProjectPage):
            return page
        project_page = page.get_ancestors().type(ProjectPage).first()
        if project_page:
            return project_page

    def get_context(self, context, **kwargs):
        page = context.get('page')
        project_page = self.get_project_page(page)
        nodes = self.get_nodes(context, root_page=project_page) + self.get_language_and_search_context()
        request = context.get('request')
        if request:
            user = request.user
        else:
            user = None
        profile_links = get_profile_links(user)
        if project_page:
            depth = 2
            brand2 = {
                # TODO: add project_page.logo migration!
                # 'src': '',
                'name': project_page.title,
                'href': project_page.url,
            }
        else:
            depth = 1
            brand2 = {}
        return {
            'id': '1',
            'toplinks': get_social_links() + get_extra_links(context) + [profile_links] + self.get_language_and_search_context(only_xs=False),
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
class Footer(InclusionTag):
    name = 'footer'
    template = 'widgets/footer.html'

    def get_context(self, context, **kwargs):
        request = context.get('request')
        if request:
            user = request.user
        else:
            user = None
        profile_links = get_profile_links(user, onlyxs=True)
        links = get_social_links(onlyxs=True) + get_extra_links(context, onlyxs=True) + [
            profile_links,
            {'href': slugurl(context, 'imprint') or '#imprint', 'text': _('Legal Disclaimer'), },
            {'href': slugurl(context, 'contact') or '#contact', 'text': _('Contact'), },
        ]
        return {'links': links}


@register.tag
class Carousel(InclusionTag):
    name = 'carousel'
    template = 'widgets/carousel-widgetchooser.html'

    def render(self, context):
        if self.get_images(context):
            return super().render(context)
        return ''

    def get_images(self, context):
        header = context.get('header')
        if header:
            return header.get('images', [])

    def get_context(self, context, **kwargs):
        items = []
        for image in self.get_images(context):
            items.append({'src': image.value.get_rendition('fill-1800x600').url})
        return {'items': items, 'id': 'header'}


@register.tag
class Overlay(InclusionTag):
    name = 'overlay'
    template = 'widgets/page-lead-overlay.html'

    def get_context(self, context, **kwargs):
        header = context.get('header')
        if not header:
            page = context.get('page')
            if page:
                return {
                    'heading': page.seo_title or page.title,
                    'lead': page.lead if hasattr(page, 'lead') else '',
                    'noimage': True,
                }
        return {
            'heading': header.get('title'),
            'heading_iconsrc': header.get('iconsrc'),
            'lead': header.get('content'),
            'noimage': not header.get('images'),
        }
