from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from wocat.cms.models import HeaderPageMixin, UniquePageMixin
from wocat.core.blocks import CORE_BLOCKS


class Entry(index.Indexed, models.Model):
    title = models.CharField(
        _('Title'),
        max_length=255,
        unique=True
    )
    slug = AutoSlugField(
        populate_from='title'
    )
    description = models.TextField(
        _('Description'),
    )
    acronym = models.BooleanField(
        _('Is an acronym'),
        default=False,
    )

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('glossary:detail', args=[self.slug])

    panels = [
        FieldPanel('title'),
        # FieldPanel('slug'),
        FieldPanel('description'),
        FieldPanel('acronym'),
    ]

    search_fields = [
        index.SearchField('title'),
        index.SearchField('description'),
        index.FilterField('acronym'),
    ]


class GlossaryPage(UniquePageMixin, HeaderPageMixin, Page):
    template = 'pages/glossary.html'

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
        verbose_name = _('Glossary')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['entries'] = Entry.objects.all()
        return context
