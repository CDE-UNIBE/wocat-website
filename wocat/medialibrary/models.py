from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import QueryDict
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Q, QuerySet
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from wocat.cms.models import UniquePageMixin, HeaderPageMixin
from wocat.core.blocks import CORE_BLOCKS

from wocat.countries.models import Continent, Country
from wocat.languages.models import Language


class MediaLibraryPage(UniquePageMixin, HeaderPageMixin, Page):
    template = 'medialibrary/library.html'
    ajax_template = 'medialibrary/library_items.html'
    ordering = ('title',)
    paginate_by = 12  # 3 rows with 4 items
    page_kwarg = 'page'

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
        verbose_name = _('Media Library')

    parent_page_types = ['cms.HomePage']

    # subpage_types = ['medialibrary.MediaPage']

    def get_queryset(self):
        return Media.objects.all().order_by(*self.ordering)

    def paginate_queryset(
            self, query_dict: QueryDict, queryset: QuerySet, page_size: int)\
            -> tuple:
        """
        Paginate a queryset and return useful objects for pagination in template
        """
        paginator = Paginator(queryset, page_size)
        page = query_dict.get(self.page_kwarg)
        try:
            page = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page = paginator.page(paginator.num_pages)
        return paginator, page, page.object_list, page.has_other_pages()

    @staticmethod
    def filter_queryset(queryset: QuerySet, query_dict: QueryDict) -> QuerySet:
        """
        Apply filters based on query parameters to the queryset.
        """
        filters = (
            # query_kwarg, filter_kwarg, cast_to
            ('type', 'media_type', int),
            ('language', 'languages__code', str),
            ('continent', 'continent', int),
            ('since', 'year__gte', int),
            ('until', 'year__lte', int),
            ('country', 'countries__code', str),
        )
        for query_kwarg, filter_kwarg, cast_to in filters:
            filter_param = query_dict.get(query_kwarg)
            if not filter_param:
                continue
            try:
                filter_param = cast_to(filter_param)
            except (TypeError, ValueError) as _:
                filter_param = None
            if filter_param:
                filter_query = {filter_kwarg: filter_param}
                queryset = queryset.filter(**filter_query)

        search = query_dict.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(abstract__icontains=search) |
                Q(author__icontains=search) | Q(content__icontains=search))

        return queryset

    @staticmethod
    def get_available_filters() -> dict:
        """
        Get all available filter values.
        """
        present_languages = Media.objects.values_list(
            'languages', flat=True).distinct()
        present_countries = Media.objects.values_list(
            'countries', flat=True).distinct()
        return {
            'types': MediaType.objects.all(),
            'languages': Language.objects.filter(pk__in=present_languages),
            'years': Media.objects.values_list('year', flat=True).distinct(
                'year').order_by('year'),
            'continents': Continent.objects.all(),
            'countries': Country.objects.filter(pk__in=present_countries),
        }

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        queryset = self.get_queryset()

        if request.is_ajax():
            query_dict = request.POST
        else:
            query_dict = request.GET
            context.update(**self.get_available_filters())

        queryset = self.filter_queryset(queryset, query_dict)
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            query_dict, queryset, self.paginate_by)

        context.update({
            'paginator': paginator,
            'page_obj': page,
            'is_paginated': is_paginated,
            'items': queryset,
        })

        return context


@register_snippet
class MediaType(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
        unique=True,
    )
    icon = models.CharField(
        _('Icon name'),
        max_length=255,
        help_text=_('Fontawesome icon name.'),
        blank=True,
    )
    default_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Default image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    order = models.PositiveIntegerField(default=None, null=True)

    class Meta:
        ordering = ['order', 'name']

    @property
    def image(self):
        return self.default_image

    def __str__(self):
        return self.name

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
        ImageChooserPanel('default_image'),
        FieldPanel('order'),
    ]


class Media(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=255,
        unique=True
    )
    abstract = models.TextField(
        _('Abstract'),
        blank=True
    )
    teaser_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Teaser image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def image(self):
        return self.teaser_image or self.media_type.image

    video = models.URLField(
        verbose_name=_('Video'),
        blank=True,
    )

    year = models.PositiveIntegerField(
        _('Year'),
        default=timezone.now().year,
        validators=[MaxValueValidator(4000)],
        blank=True, null=True
    )

    languages = models.ManyToManyField(
        verbose_name=_('Languages'),
        to=Language,
        blank=True
    )

    content = StreamField(
        CORE_BLOCKS,
        blank=True,
    )
    file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True, blank=True,
        on_delete=models.PROTECT,
        related_name='+',
        help_text=_('This field is only used if the content is empty.'),
    )
    author = models.CharField(
        _('Author'),
        max_length=255,
        blank=True,
    )
    countries = models.ManyToManyField(
        verbose_name=_('Countries'),
        to=Country,
        blank=True,
    )
    continent = models.ForeignKey(
        to=Continent,
        blank=True, null=True,
    )
    media_type = models.ForeignKey(
        'MediaType',
        verbose_name=_('Type'),
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('media:detail', args=[self.id])

    panels = [
        FieldPanel('title'),
        FieldPanel('abstract'),
        FieldPanel('media_type'),
        FieldPanel('video'),
        DocumentChooserPanel('file'),
        ImageChooserPanel('teaser_image'),
        FieldPanel('author'),
        FieldPanel('countries'),
        FieldPanel('continent'),
        FieldPanel('year'),
        FieldPanel('languages'),
        StreamFieldPanel('content'),
    ]
