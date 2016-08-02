from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import ProgrammingError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from wocat.cms.blocks import IMAGE_BLOCKS, OverlayTeaserMapBlock
from wocat.core.blocks import CORE_BLOCKS

__author__ = 'Eraldo Energy'


class UniquePageMixin:
    """
    Mixin for Wagtail pages to make sure only one of this Page exists.
    """

    @classmethod
    def clean_parent_page_models(cls):
        # Only allow a single instance.
        try:
            if cls.objects and cls.objects.exists():
                return []
        except ProgrammingError:  # not migrated yet.
            pass
        return super().clean_parent_page_models()


class HeaderPageMixin(models.Model):
    header_images = StreamField(
        IMAGE_BLOCKS,
        blank=True
    )
    lead = models.TextField(
        _('Lead text'),
        blank=True
    )

    class Meta:
        abstract = True

    content_panels = [
        MultiFieldPanel(
            [
                StreamFieldPanel('header_images'),
                FieldPanel('lead'),
            ],
            heading="Header",
            classname="collapsible collapsed"
        ),
    ]

    search_fields = (
        index.SearchField('lead'),
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['header'] = {
            'title': self.seo_title or self.title,
            'images': self.header_images,
            'noimage': not bool(self.header_images),
            'content': self.lead,
        }
        return context


class ContentPage(HeaderPageMixin, Page):
    template = 'pages/content.html'

    content = StreamField(
        CORE_BLOCKS,
        blank=True
    )

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + (
        index.SearchField('content'),
    )

    class Meta:
        verbose_name = _('Content')


class HomePage(UniquePageMixin, HeaderPageMixin, Page):
    template = 'pages/home.html'

    content = StreamField(
        CORE_BLOCKS + [('map_teaser', OverlayTeaserMapBlock())],
        blank=True
    )

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + (
        index.SearchField('content'),
    )

    class Meta:
        verbose_name = _('Home')

        # parent_page_types = ['Root']
        # subpage_types = ['ProjectPage']


class ProjectsAndCountiesPage(UniquePageMixin, Page):
    template = 'pages/content.html'

    class Meta:
        verbose_name = _('Projects & Countries')

    parent_page_types = ['HomePage']
    subpage_types = ['ProjectsPage', 'CountriesPage']


class ProjectsPage(UniquePageMixin, Page):
    template = 'pages/content.html'

    class Meta:
        verbose_name = _('Projects')

    parent_page_types = ['ProjectsAndCountiesPage']
    subpage_types = ['ProjectPage']


class ProjectPage(HeaderPageMixin, Page):
    template = 'pages/content.html'

    content = StreamField(CORE_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Project')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + (
        index.SearchField('content'),
    )

    parent_page_types = ['ProjectsPage']
    subpage_types = ['ContentPage']


class CountriesPage(UniquePageMixin, Page):
    template = 'pages/content.html'

    class Meta:
        verbose_name = _('Countries')

    parent_page_types = ['ProjectsAndCountiesPage']
    subpage_types = ['CountryPage']


class CountryPage(HeaderPageMixin, Page):
    template = 'pages/country.html'

    country = CountryField(unique=True)

    @property
    def flag(self):
        if hasattr(self, 'country'):
            return self.country.flag

    contact_person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    content = StreamField(CORE_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Country')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        FieldPanel('country'),
        FieldPanel('contact_person'),
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + (
        index.SearchField('content'),
    )

    parent_page_types = ['CountriesPage']
    subpage_types = ['ContentPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        header = context.get('header')
        if header:
            header['iconsrc'] = self.flag
        return context


class MembersPage(UniquePageMixin, Page):
    template = 'pages/members.html'

    content = StreamField(CORE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('content'),
    )

    # parent_page_types = []
    # subpage_types = []

    class Meta:
        verbose_name = _('Members')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        members = []
        countries = []
        expertises = []
        # TODO: Update to users with group 'Members' only.
        users = get_user_model().objects.all()
        for user in users:
            countries.append({'name': user.country.name})
            # expertises.append({'name': user.expertise})
            members.append({
                'avatarsrc': user.avatar.url if user.avatar else '',
                'country': user.country.name if user.country else '',
                # 'expertises': [{'name': user.expertise}] if user.expertise else '',
                'name': user.username or '',
                'organisation': user.organisation or '',
                # 'position': 'Manager',
                'url': user.get_absolute_url(),
                'visible': True,
            })
        context.update(
            {'countries': countries,
             # 'expertises': expertises,
             'members': members,
             # TODO: set and calculate pages
             # 'maxpagesize': 3,
             # 'pages': [1, 2, 3, 4],
             }
        )
        return context


class NewsAndEventsPage(UniquePageMixin, Page):
    template = 'pages/content.html'

    class Meta:
        verbose_name = _('News & Events')

    parent_page_types = ['HomePage']
    subpage_types = ['news.NewsIndexPage']
