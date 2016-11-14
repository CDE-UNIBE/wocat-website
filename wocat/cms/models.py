from math import ceil

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import ProgrammingError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel, InlinePanel, \
    PageChooserPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailsearch import index

from wocat.cms.blocks import IMAGE_BLOCKS, OverlayTeaserMapBlock
from wocat.core.blocks import CORE_BLOCKS
from wocat.countries.models import Country
from wocat.institutions.models import Institution
from wocat.users.blocks import CONTACT_PERSON_TEASER_BLOCKS

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


class ContentPage(HeaderPageMixin, Page):
    template = 'pages/content.html'

    content = StreamField(
        CORE_BLOCKS,
        blank=True
    )

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Content')


class HomePage(UniquePageMixin, HeaderPageMixin, Page):
    template = 'pages/home.html'

    about_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    about_link_text = models.CharField(
        _('About link text'),
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
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Home')

        # parent_page_types = ['Root']
        # subpage_types = ['ProjectPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if self.about_page:
            context['links'] = [
                {'href': self.about_page.url, 'text': self.about_link_text}
            ]
        return context


class ProjectsAndCountiesPage(UniquePageMixin, HeaderPageMixin, Page):
    template = 'pages/projects_and_countries.html'

    content = StreamField(CORE_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Projects & Countries')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

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


class ProjectsPage(UniquePageMixin, Page):
    template = 'projects/index.html'

    class Meta:
        verbose_name = _('Projects')

    parent_page_types = ['ProjectsAndCountiesPage']
    subpage_types = ['ProjectPage']

    @property
    def projects(self):
        return self.get_children()


class ProjectPage(HeaderPageMixin, Page):
    template = 'pages/content.html'

    contact_person = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='project_contact',
        verbose_name=_('Contact person'),
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )

    content = StreamField(CORE_BLOCKS + CONTACT_PERSON_TEASER_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Project')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        FieldPanel('contact_person'),
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['ProjectsPage']
    subpage_types = ['ContentPage', 'ProjectCountriesPage', 'NewsAndEventsPage']

    @property
    def countries(self):
        return self.get_descendants().type(ProjectCountryPage).specific()


class ProjectCountriesPage(HeaderPageMixin, Page):
    template = 'countries/index.html'

    content = StreamField(
        CORE_BLOCKS,
        blank=True
    )

    class Meta:
        verbose_name = _('Project Countries')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['ProjectPage']
    subpage_types = ['ProjectCountryPage']

    @property
    def countries(self):
        return self.get_children()


class ProjectCountryPage(HeaderPageMixin, Page):
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
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.FilterField('country'),
        index.SearchField('content'),
    ]

    parent_page_types = ['ProjectCountriesPage']
    subpage_types = ['ContentPage']


class CountriesPage(UniquePageMixin, Page):
    template = 'countries/index.html'

    class Meta:
        verbose_name = _('Countries')

    parent_page_types = ['ProjectsAndCountiesPage']
    subpage_types = ['CountryPage']

    @property
    def countries(self):
        return self.get_children()


class CountryPage(HeaderPageMixin, Page):
    template = 'pages/country.html'

    country = models.OneToOneField(
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
    content = StreamField(CORE_BLOCKS + CONTACT_PERSON_TEASER_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('Country')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        FieldPanel('country'),
        FieldPanel('contact_person'),
        StreamFieldPanel('content'),
    ]

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
        return context


class RegionsPage(UniquePageMixin, Page):
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


class RegionPage(HeaderPageMixin, Page):
    template = 'pages/region.html'

    contact_person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='region_contact',
        verbose_name=_('Contact person'),
        on_delete=models.SET_NULL,
        null=True
    )

    content = StreamField(CORE_BLOCKS + CONTACT_PERSON_TEASER_BLOCKS, blank=True)

    @property
    def countries(self):
        countries = [country.country for country in self.region_countries.all()]
        return countries

    @property
    def country_codes(self):
        return [country.country.code for country in self.countries]

    class Meta:
        verbose_name = _('Region')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        InlinePanel('region_countries', label="Countries"),
        FieldPanel('contact_person'),
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        # index.FilterField('countries'), TODO: This can't be indexed
        index.SearchField('content'),
    ]

    parent_page_types = ['RegionsPage']
    subpage_types = []


class MembersPage(UniquePageMixin, Page):
    template = 'pages/members.html'
    paginate_by = 20

    content = StreamField(CORE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    # parent_page_types = []
    # subpage_types = []

    class Meta:
        verbose_name = _('Members')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        members = []
        countries = []
        expertises = []
        organisations = []
        users = get_user_model().objects.filter(is_active=True)
        for user in users:
            if user.country:
                countries.append({'name': user.country.name})
            expertises += [{'name': experience} for experience in user.experiences.all()]
            if user.institution:
                organisations.append({'name': user.institution})
            members.append({
                'avatarsrc': user.avatar.url if user.avatar else '',
                'country': user.country.name if user.country else '',
                'expertises': expertises,
                'name': user.name or '',
                'organisation': user.institution or '',
                'position': user.position or '',
                'href': user.get_absolute_url(),
                'url': user.get_absolute_url(),
                'visible': True,
            })
        context.update({
            'allcountries': 'All Countries',
            'allexpertises': 'All Expertiese',
            'allorganisations': 'All Organisations',
            'countries': countries,
            'expertises': expertises,
            'organisations': organisations,
            'members': members,
        })

        # Pagination
        user_count = users.count()
        if user_count:
            per_page = self.paginate_by
            context.update({
                # Calculate pages
                'maxpagesize': per_page,
                'pages': [number + 1 for number in range(ceil(user_count / per_page))],
            })

        return context


class InstitutionsPage(UniquePageMixin, Page):
    template = 'pages/institutions.html'
    paginate_by = 20

    content = StreamField(CORE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['MembersPage']

    # subpage_types = []

    class Meta:
        verbose_name = _('Institutional Members')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        institutions = Institution.objects.filter(memorandum=True)
        context['institutions'] = institutions

        members = []
        countries = []
        contacts = []
        years = institutions.values_list('year', flat=True)
        for institution in institutions:
            countries.append({'name': institution.country.name})
            members.append({
                'avatarsrc': institution.logo.get_rendition('max-1200x1200').url if institution.logo else '',
                'country': institution.country.name if institution.country else '',
                'name': institution.name or '',
                'url': institution.get_absolute_url(),
                'visible': True,
            })
            if institution.year:
                years.append({'value': institution.year})

        context.update({
            'allcountries': 'All Countries',
            'allyears': 'All Years',
            'allcontacts': 'All Contacts',
            'members': members,
            'countries': countries,
            'contacts': contacts,
            'years': years,
        })

        # Pagination
        member_count = institutions.count()
        if member_count:
            per_page = self.paginate_by
            context.update({
                # Calculate pages
                'maxpagesize': per_page,
                'pages': [number + 1 for number in range(ceil(member_count / per_page))],
            })

        return context


class NewsAndEventsPage(HeaderPageMixin, Page):
    template = 'pages/content.html'

    content = StreamField(CORE_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('News & Events')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    def get_news_page_model(self):
        from wocat.news.models import NewsPage
        return NewsPage

    parent_page_types = ['HomePage', 'ProjectPage']
    subpage_types = ['news.NewsIndexPage']

    @property
    def news(self):
        NewsPage = self.get_news_page_model()
        return self.get_descendants().type(NewsPage).specific()
        #
        # @property
        # def events(self):
        #     return []  # TODO: Waiting for Events pages to be implemented.
