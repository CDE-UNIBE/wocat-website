from django.conf import settings
from django.db import ProgrammingError
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import translation, timezone
from django.utils.translation import ugettext_lazy as _
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, \
    MultiFieldPanel, FieldPanel, InlinePanel, \
    PageChooserPanel
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailsearch import index

from wocat.cms.blocks import IMAGE_BLOCKS, OverlayTeaserMapBlock, \
    PROJECT_BLOCKS, REGION_BLOCKS, COUNTRY_BLOCKS, EVENTS_BLOCKS
from wocat.cms.translation import TranslatablePageMixin
from wocat.core.blocks import CORE_BLOCKS
from wocat.countries.models import Country
from wocat.users.models import UserExperience

__author__ = 'Eraldo Energy'


def get_default_year_now():
    return timezone.now().year


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
    lead = RichTextField(
        'Lead text',
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

    search_fields = [
        index.SearchField('lead'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['header'] = {
            'title': self.seo_title or self.title,
            'images': self.header_images,
            'noimage': not bool(self.header_images),
            'content': self.lead,
        }
        return context


class ContentPage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'pages/content.html'

    content = StreamField(
        CORE_BLOCKS,
        blank=True
    )

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = 'Content'


class HomePage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'pages/home.html'

    about_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    about_link_text = models.CharField(
        'About link text',
        blank=True,
        max_length=255,
    )

    content = StreamField(
        CORE_BLOCKS + [('map_teaser', OverlayTeaserMapBlock())],
        blank=True
    )

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        MultiFieldPanel(
            [
                PageChooserPanel('about_page', 'cms.ContentPage'),
                FieldPanel('about_link_text'),
            ],
            heading="About",
            classname="collapsible collapsed"
        ),
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Home')

        # parent_page_types = ['Root']
        # subpage_types = ['ProjectPage']

    def serve(self, request, **kwargs):
        language = translation.get_language_from_request(request)

        # There can be multiple "HomePage"s (basically one for each existing
        # language), therefore we need to check if the current one is already
        # prefixed with the language. In this case, no additional redirect is
        # necessary.
        for lang_prefix in [l[0] for l in settings.LANGUAGES]:
            if self.url.startswith('/' + lang_prefix):
                return super().serve(request, **kwargs)

        return HttpResponseRedirect(self.url + language + '/')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if self.about_page:
            context['links'] = [
                {'href': self.about_page.url, 'text': self.about_link_text}
            ]
        return context


class ProjectsAndCountiesPage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'pages/content.html'

    content = StreamField(CORE_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Projects & Countries')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['HomePage']
    subpage_types = ['ProjectsPage', 'CountriesPage', 'RegionsPage']

    @property
    def projects(self):
        return self.get_descendants().type(ProjectPage).specific()

    @property
    def countries(self):
        return self.get_descendants().type(CountryPage).specific()

    @property
    def regions(self):
        return self.get_descendants().type(RegionPage).specific()


class ProjectsPage(TranslatablePageMixin, Page):
    template = 'projects/index.html'

    class Meta:
        verbose_name = _('Projects')

    parent_page_types = ['ProjectsAndCountiesPage']
    subpage_types = ['ProjectPage']

    @property
    def projects(self):
        return self.get_children()


class ProjectPage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'pages/content.html'

    contact_person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='project_contact',
        verbose_name=_('Contact person'),
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    included_countries = ParentalManyToManyField(
        verbose_name=_('Countries without country page'),
        to=Country,
        blank=True,
    )

    content = StreamField(PROJECT_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Project')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        FieldPanel('contact_person'),
        StreamFieldPanel('content'),
        FieldPanel('included_countries'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ] + TranslatablePageMixin.search_fields

    parent_page_types = ['ProjectsPage']
    subpage_types = ['ContentPage', 'ProjectCountriesPage', 'NewsAndEventsPage']

    @property
    def countries(self):
        return self.get_descendants().type(ProjectCountryPage).specific()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['contact_person'] = self.contact_person
        context['map_initial_url'] = self.get_api_detail_url()
        return context

    def get_api_detail_url(self):
        return reverse_lazy('projectpage-detail', kwargs={'pk': self.pk})


class ProjectCountriesPage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'countries/index.html'

    content = StreamField(
        CORE_BLOCKS,
        blank=True
    )

    class Meta:
        verbose_name = _('Project Countries')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['ProjectPage']
    subpage_types = ['ProjectCountryPage']

    @property
    def countries(self):
        return self.get_children()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['map_initial_url'] = self.get_api_detail_url()
        return context

    def get_api_detail_url(self):
        return reverse_lazy(
            'projectpage-detail', kwargs={'pk': self.get_parent().pk})


class ProjectCountryPage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'pages/content.html'

    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
    )

    @property
    def flag(self):
        if hasattr(self, 'country'):
            return self.country.flag

    @property
    def code(self):
        if hasattr(self, 'country'):
            return self.country.code

    content = StreamField(
        CORE_BLOCKS,
        blank=True
    )

    class Meta:
        verbose_name = _('Project Country')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        FieldPanel('country'),
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.FilterField('country'),
        index.SearchField('content'),
    ]

    parent_page_types = ['ProjectCountriesPage']
    subpage_types = ['ContentPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['map_initial_url'] = self.country.get_api_detail_url()
        return context


class CountriesPage(TranslatablePageMixin, Page):
    template = 'countries/index.html'

    class Meta:
        verbose_name = _('Countries')

    parent_page_types = ['ProjectsAndCountiesPage']
    subpage_types = ['CountryPage']

    @property
    def countries(self):
        return self.get_children()


class CountryPage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'pages/country.html'

    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
    )

    @property
    def flag(self):
        if hasattr(self, 'country'):
            return self.country.flag

    @property
    def code(self):
        if hasattr(self, 'country'):
            return self.country.code

    contact_person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='country_contact',
        verbose_name=_('Contact person'),
        on_delete=models.SET_NULL,
        null=True
    )
    content = StreamField(COUNTRY_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Country')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        FieldPanel('country'),
        FieldPanel('contact_person'),
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['CountriesPage']
    subpage_types = ['ContentPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        header = context.get('header')
        if header:
            header['iconsrc'] = self.flag
        context['contact_person'] = self.contact_person
        context['map_initial_url'] = self.get_api_detail_url()
        return context

    def get_api_detail_url(self):
        return '{url}?country_code={country_code}'.format(
            url=reverse_lazy('country-detail'),
            country_code=self.code
        )


class RegionsPage(TranslatablePageMixin, Page):
    template = 'pages/content.html'

    class Meta:
        verbose_name = _('Regions')

    parent_page_types = ['ProjectsAndCountiesPage']
    subpage_types = ['RegionPage']


class RegionCountry(Orderable):
    page = ParentalKey('RegionPage', related_name='region_countries')
    country = models.ForeignKey(CountryPage, related_name='+')
    panels = [
        FieldPanel('country'),
    ]


class RegionPage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'pages/region.html'

    contact_person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='region_contact',
        verbose_name=_('Contact person'),
        on_delete=models.SET_NULL,
        null=True
    )

    content = StreamField(REGION_BLOCKS, blank=True)

    @property
    def countries(self):
        countries = [country.country for country in self.region_countries.all()]
        return countries

    @property
    def country_codes(self):
        return [country.country.code for country in self.countries]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['contact_person'] = self.contact_person
        context['map_initial_url'] = self.get_api_detail_url()
        return context

    class Meta:
        verbose_name = _('Region')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        InlinePanel('region_countries', label="Countries"),
        FieldPanel('contact_person'),
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        # index.FilterField('countries'), TODO: This can't be indexed
        index.SearchField('content'),
    ] + TranslatablePageMixin.search_fields

    parent_page_types = ['RegionsPage']
    subpage_types = []

    def get_api_detail_url(self):
        return reverse_lazy('regionpage-detail', kwargs={'pk': self.pk})


class MembersPage(UniquePageMixin, TranslatablePageMixin, Page):
    template = 'pages/members.html'
    paginate_by = 100

    content = StreamField(CORE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Members')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['countries'] = Country.objects.filter(
            user__isnull=False
        ).distinct().values_list(
            'code', 'name'
        )
        from wocat.institutions.models import Institution
        context['institutions'] = Institution.objects.filter(
            user__isnull=False
        ).distinct().values_list(
            'pk', 'name'
        )
        context['experiences'] = UserExperience.objects.all()
        return context


class InstitutionsPage(UniquePageMixin, TranslatablePageMixin, Page):
    template = 'pages/institutions.html'
    paginate_by = 100

    content = StreamField(CORE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Institutional Members')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['countries'] = [
            (c.code, str(c)) for c in Country.objects.filter(
                institution__isnull=False).distinct()]
        return context


class NewsAndEventsPage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'pages/content.html'

    content = StreamField(CORE_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('News & Events')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    def get_news_page_model(self):
        from wocat.news.models import NewsPage
        return NewsPage

    parent_page_types = ['HomePage', 'ProjectPage']
    subpage_types = ['news.NewsIndexPage', 'EventsPage']

    @property
    def news(self):
        NewsPage = self.get_news_page_model()
        return self.get_descendants().type(NewsPage).specific()
        #
        # @property
        # def events(self):
        #     return []  # TODO: Waiting for Events pages to be implemented.


class EventsPage(HeaderPageMixin, TranslatablePageMixin, Page):
    template = 'pages/events.html'

    content = StreamField(EVENTS_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Events')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['NewsAndEventsPage']
    subpage_types = []


@register_setting
class TopNavigationSettings(ClusterableModel, BaseSetting):
    panels = [
        InlinePanel('social_media_links', label="Social Links"),
        InlinePanel('top_navigation_links', label="Top Links"),
    ]

    class Meta:
        verbose_name = 'Top navigation settings'


class TopNavigationLink(Orderable, models.Model):
    navigation = ParentalKey(TopNavigationSettings, related_name='top_navigation_links')
    target = models.ForeignKey(
        'wagtailcore.Page',
        help_text='Always link the original page (in English)!')

    @property
    def url(self):
        return self.target.url

    panels = [
        PageChooserPanel('target'),
    ]


class SocialMediaLink(Orderable, models.Model):
    navigation = ParentalKey(TopNavigationSettings, related_name='social_media_links')
    icon = models.CharField(
        max_length=255,
        help_text='Fontawesome icon name'
    )
    url = models.URLField(
        help_text='Your social media page URL'
    )

    panels = [
        FieldPanel('icon'),
        FieldPanel('url'),
    ]


@register_setting
class FooterSettings(ClusterableModel, BaseSetting):
    content = StreamField(
        CORE_BLOCKS,
        blank=True
    )

    panels = [
        InlinePanel('footer_links', label=_("Links")),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Footer settings'


class FooterLink(Orderable, models.Model):
    footer = ParentalKey(FooterSettings, related_name='footer_links')
    target = models.ForeignKey(
        'wagtailcore.Page',
        help_text='Always link the original page (in English)!')

    @property
    def url(self):
        return self.target.url

    panels = [
        PageChooserPanel('target'),
    ]


@register_setting
class TermsSettings(BaseSetting):
    _name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        blank=True,
        help_text='The name of the selected page will be used if this field is left empty.'
    )
    target = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL
    )

    @property
    def name(self):
        return self._name or self.target

    panels = [
        FieldPanel('_name'),
        PageChooserPanel('target'),
    ]

    class Meta:
        verbose_name = 'Terms settings'
