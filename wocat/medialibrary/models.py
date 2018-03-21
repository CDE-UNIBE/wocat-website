from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import QueryDict
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import QuerySet
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from wocat.cms.models import UniquePageMixin, HeaderPageMixin, \
    get_default_year_now
from wocat.cms.translation import TranslatablePageMixin
from wocat.core.blocks import CORE_BLOCKS

from wocat.countries.models import Continent, Country
from wocat.languages.models import Language


class MediaLibraryPage(
        UniquePageMixin, HeaderPageMixin, TranslatablePageMixin, Page):
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
    ] + TranslatablePageMixin.content_panels

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = 'Media Library'

    parent_page_types = ['cms.HomePage']

    # subpage_types = ['medialibrary.MediaPage']

    def get_queryset(self):
        return Media.objects.all()

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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        if request.is_ajax():
            query_dict = request.POST
        else:
            query_dict = request.GET

        from wocat.medialibrary.filters import MediaLibraryFilter
        media_filter = MediaLibraryFilter(
            query_dict, queryset=self.get_queryset())

        paginator, page, queryset, is_paginated = self.paginate_queryset(
            query_dict, media_filter.qs.order_by(*self.ordering),
            self.paginate_by)

        context.update({
            'media_filter': media_filter,
            'paginator': paginator,
            'page_obj': page,
            'is_paginated': is_paginated,
            'items': queryset,
        })

        return context


class Media(models.Model):

    MEDIA_TYPES = Choices(
        (3, _('Books')),
        (4, _('Maps')),
        (8, _('Other documents')),
        (6, _('Photos')),
        (10, _('PR materials')),
        (9, _('Presentations')),
        (1, _('SLM questionnaires')),
        (2, _('Training materials')),
        (5, _('Videos')),
    )

    title = models.CharField(
        'Title',
        max_length=255,
        unique=True
    )
    abstract = models.TextField(
        'Abstract',
        blank=True
    )
    teaser_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Teaser image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def image(self):
        return self.teaser_image or None

    video = models.URLField(
        verbose_name='Video',
        blank=True,
    )

    year = models.PositiveIntegerField(
        'Year',
        default=get_default_year_now,
        validators=[MaxValueValidator(4000)],
        blank=True, null=True
    )

    languages = models.ManyToManyField(
        verbose_name='Languages',
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
        help_text='This field is only used if the content is empty.',
    )
    author = models.CharField(
        'Author',
        max_length=255,
        blank=True,
    )
    countries = models.ManyToManyField(
        verbose_name='Countries',
        to=Country,
        blank=True,
    )
    continent = models.ForeignKey(
        to=Continent,
        blank=True, null=True,
    )
    media_type = models.IntegerField(
        choices=MEDIA_TYPES, db_column='media_type_id')

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'

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
