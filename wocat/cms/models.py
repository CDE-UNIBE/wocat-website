from django.conf import settings
from django.db import ProgrammingError
from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from wocat.cms.blocks import CORE_BLOCKS, IMAGE_BLOCKS

__author__ = 'Eraldo Energy'


class UniquePageMixin(object):
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


class ContentPage(Page):
    template = 'pages/content.html'

    content = StreamField(CORE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = _('Content')


class HomePage(UniquePageMixin, Page):
    template = 'pages/content.html'

    content = StreamField(CORE_BLOCKS, blank=True)
    header_images = StreamField(IMAGE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                StreamFieldPanel('header_images'),
            ],
            heading="Header",
            classname="collapsible collapsed"
        ),
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + (
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


class ProjectPage(Page):
    template = 'pages/content.html'

    class Meta:
        verbose_name = _('Countries')

    parent_page_types = ['ProjectsPage']
    subpage_types = ['ContentPage']


class CountriesPage(UniquePageMixin, Page):
    template = 'pages/content.html'

    class Meta:
        verbose_name = _('Countries')

    parent_page_types = ['ProjectsAndCountiesPage']
    subpage_types = ['CountryPage']


class CountryPage(Page):
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
    per_capita_income = models.CharField(
        _('Per capita income'),
        max_length=100,
        blank=True,
    )
    population = models.CharField(
        _('Population'),
        max_length=100,
        blank=True,
    )
    human_development_index = models.CharField(
        _('Human development index'),
        max_length=100,
        blank=True,
    )
    poverty_rate = models.CharField(
        _('Poverty rate'),
        max_length=100,
        blank=True,
    )
    header_images = StreamField(IMAGE_BLOCKS, blank=True)
    content = StreamField(CORE_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Country')

    content_panels = Page.content_panels + [
        FieldPanel('country'),
        FieldPanel('contact_person'),
        MultiFieldPanel(
            [
                StreamFieldPanel('header_images'),
                FieldPanel('per_capita_income'),
                FieldPanel('population'),
                FieldPanel('human_development_index'),
                FieldPanel('poverty_rate'),
            ],
            heading="Header",
            classname="collapsible collapsed"
        ),
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('content'),
    )

    parent_page_types = ['CountriesPage']
    subpage_types = ['ContentPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['carousel_images'] = self.header_images
        context['heading'] = self.title
        context['heading_iconsrc'] = self.flag
        meta_objects = [(self._meta.get_field(field).verbose_name, getattr(self, field)) for field in
                        ('per_capita_income', 'population', 'human_development_index', 'poverty_rate') if
                        hasattr(self, field)]
        context['lead'] = render_to_string('widgets/country-meta.html', context={'objects': meta_objects})
        return context
