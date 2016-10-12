from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from wocat.core.blocks import CORE_BLOCKS
from wocat.cms.models import HeaderPageMixin


class NewsIndexPage(HeaderPageMixin, Page):
    template = 'news/index.html'

    content = StreamField(CORE_BLOCKS, blank=True)

    class Meta:
        verbose_name = _('News index')

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['cms.NewsAndEventsPage']
    subpage_types = ['NewsPage']

    @property
    def news(self):
        news = NewsPage.objects.descendant_of(self)
        return news.order_by('-date')


class NewsPage(HeaderPageMixin, Page):
    template = 'news/article.html'

    content = StreamField(
        CORE_BLOCKS,
        blank=True
    )

    author = models.CharField(
        _('Author'),
        max_length=255,
        blank=True,
    )

    date = models.DateField(
        _('Date'),
        default = timezone.now,
    )

    # countries = models.ManyToManyField(
    #     Country,
    # )

    @property
    def lead_image(self):
        images = self.header_images
        if images:
            return images[0].value

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
        FieldPanel('author'),
        FieldPanel('date'),
        # FieldPanel('countries'),
        # InlinePanel('countries', label=_('Countries')),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        # index.FilterField('countries'),
        index.SearchField('content'),
    ]

    parent_page_types = ['NewsIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title


    # class NewsPageCountry(models.Model):
    #     news = ParentalKey(
    #         'NewsPage',
    #         related_name='countries'
    #     )
    #     country = models.ForeignKey(
    #         'Country',
    #         related_name="+"
    #     )
    #     panels = [
    #         FieldPanel('country')
    #     ]
