from django.db import ProgrammingError
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page

from wocat.cms.blocks import CORE_BLOCKS, HEADER_BLOCKS

__author__ = 'Eraldo Energy'


class SinglePageMixin(object):
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


class HomePage(SinglePageMixin, Page):
    template = 'pages/content.html'

    content = StreamField(CORE_BLOCKS, blank=True)
    header = StreamField(HEADER_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('header'),
        StreamFieldPanel('content'),
    ]
