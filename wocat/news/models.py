from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from wocat.core.blocks import CORE_BLOCKS
from wocat.cms.models import HeaderPageMixin, UniquePageMixin


class NewsIndexPage(UniquePageMixin, Page):
    template = 'news/index.html'

    class Meta:
        verbose_name = _('News index')

    parent_page_types = ['cms.NewsAndEventsPage']
    subpage_types = ['NewsPage']


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

    @property
    def lead_image(self):
        images = self.header_images
        if images:
            return images[0].value

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
        FieldPanel('author'),
        FieldPanel('date'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    parent_page_types = ['NewsIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title
