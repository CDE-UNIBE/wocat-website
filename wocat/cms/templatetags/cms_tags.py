from classytags.helpers import InclusionTag
from django import template
from django.middleware.csrf import get_token
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.templatetags.wagtailcore_tags import richtext

from wocat.cms.models import ProjectPage, TopNavigationSettings, \
    FooterSettings
from wocat.cms.translation import TranslatablePageMixin
from wocat.core.context_processors import template_settings

register = template.Library()


def get_profile_links(user, onlyxs=False):
    if user and user.is_authenticated():
        profile_links = {
            'dropdown': True,
            'text': user.first_name or user.email,
            'links': [
                {'href': reverse('users:detail', kwargs={'pk': user.id}), 'text': _('Profile'), 'active': True},
                {'href': reverse('account_logout'), 'text': _('Logout')},
            ],
            'href': reverse('users:detail', kwargs={'pk': user.id}),
            'onlyxs': onlyxs,
        }
    else:
        profile_links = {'href': reverse('account_login'), 'text': 'Login'}
    return profile_links


def get_social_links(context, onlyxs=False):
    links = []
    settings = None
    request = context.get('request')
    if request and hasattr(request, 'site'):
        settings = TopNavigationSettings.for_site(request.site)
    if settings:
        for link in settings.social_media_links.all():
            links.append({
                'text': '<i class="fa fa-lg fa-{0}" aria-hidden="true"></i>'.format(link.icon),
                'href': link.url,
                'onlyxs': onlyxs
            })
    return links


def get_extra_links(context, onlyxs=False):
    links = []
    settings = None
    request = context.get('request')
    if request and hasattr(request, 'site'):
        settings = TopNavigationSettings.for_site(request.site)
    if settings:
        for link in settings.top_navigation_links.all():
            page = TranslatablePageMixin.get_translated_page(
                link.target.specific)
            links.append({
                'text': page.title,
                'href': page.url,
                'onlyxs': onlyxs
            })
    return links


@register.tag
class Header(InclusionTag):
    name = 'header'
    template = 'widgets/header.html'

    def get_language_and_search_context(self, only_xs=True):
        return [
            {
                'languageswitcher': True,
                'onlyxs': only_xs,
            },
            {
                'href': reverse('search:index'),
                'text': '<i class="fa fa-search" aria-hidden="true"></i>',
                'onlyxs': only_xs},
        ]

    def get_node(self, page, current_page, ancestors):
        page = TranslatablePageMixin.get_translated_page(page)
        text = page.title
        if hasattr(page, 'flag'):
            text = format_html('<strong>flag</strong>{}', text)
        return {
            'text': text,
            'href': page.url,
            # Checking if this page is in the tree of active pages
            'active': page.specific == current_page or page in ancestors,
        }

    def get_nodes(self, context, root_page=None):
        current_page = context.get('page')
        if not root_page and current_page and hasattr(
                current_page, 'get_language_homepage'):
            root_page = current_page.get_language_homepage()

        # Try to get the specific type (e.g. Homepage) of the root_page
        root_page = getattr(root_page, 'specific', root_page)

        if not root_page:
            return []

        if root_page.get_language() != TranslatablePageMixin.original_lang_code:
            # If current page is a translation, get the original to build the
            # menu
            root_page = root_page.original_page()

        main_pages = root_page.get_children().live().in_menu().specific()
        if current_page:
            current_page = current_page.specific
            ancestors = current_page.get_ancestors().live().in_menu().specific()
        else:
            ancestors = []

        return [
            self.get_node(page, current_page=current_page, ancestors=ancestors)
            for page in main_pages]

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
        if request and hasattr(request, 'user'):
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
            'toplinks': get_social_links(context) + get_extra_links(context) + [
                profile_links] + self.get_language_and_search_context(only_xs=False),
            'mainnav': {
                'depth': depth,
                # only visible if in or under a project page
                'brand2': brand2,
                'links1': nodes,
                'links2': nodes,
            },
            'csrf_token': get_token(context.get('request')),
            # Add template settings to be accessible in header
            **template_settings(context.get('request')),
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
            crumbs = [self.get_node(page, current_page=current_page, ancestors=ancestors) for page in ancestors] + [
                self.get_node(current_page, current_page=current_page, ancestors=ancestors)]
            # Manually adjust the crumbs to remove the language link and
            # correctly display translated "Home" link.
            if len(crumbs) > 2:
                del crumbs[1]
                crumbs[0]['text'] = _('Home')
            return crumbs
        else:
            return []

    def get_context(self, context, **kwargs):
        nodes = self.get_nodes(context)
        return {'links': nodes}


@register.tag
class ContentLanguageSwitcher(InclusionTag):
    """A language switcher just for the content (CMS page), not entire site!"""
    name = 'content-language-switcher'
    template = 'widgets/content-language-switcher.html'

    def get_context(self, context, **kwargs):
        try:
            translation_links = list(context.get('page').translation_links())
        except AttributeError:
            translation_links = []
        return {
            'translation_links': translation_links,
            'csrf_token': get_token(context.get('request')),
        }


@register.tag
class Footer(InclusionTag):
    name = 'footer'
    template = 'widgets/footer.html'

    def get_context(self, context, **kwargs):
        request = context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
        else:
            user = None
        profile_links = get_profile_links(user, onlyxs=True)
        links = get_social_links(context, onlyxs=True) + \
                get_extra_links(context, onlyxs=True) + \
                [profile_links] + \
                self.get_links(context)
        content = self.get_content(context)
        return {
            'links': links,
            'content': content
        }

    def get_settings(self, context):
        if context:
            request = context.get('request')
            if request and hasattr(request, 'site'):
                settings = FooterSettings.for_site(request.site)
                if settings:
                    return settings

    def get_links(self, context, onlyxs=False):
        links = []
        settings = self.get_settings(context)
        if settings:
            for link in settings.footer_links.all():
                page = TranslatablePageMixin.get_translated_page(
                    link.target.specific)
                links.append({
                    'text': page.title,
                    'href': page.url,
                    'onlyxs': onlyxs
                })
        return links

    def get_content(self, context, onlyxs=False):
        settings = self.get_settings(context)
        links = []
        if settings:
            return settings.content


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
                    'lead': richtext(page.lead) if hasattr(page, 'lead') else '',
                    'noimage': True,
                }
        return {
            'heading': header.get('title'),
            'heading_iconsrc': header.get('iconsrc'),
            'lead': richtext(header.get('content')) if header.get('content') else '',
            'noimage': not header.get('images'),
        }
