from django.core.urlresolvers import reverse
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from wocat.cms.models import UniquePageMixin
from wocat.core.blocks import CORE_BLOCKS


# class MediaLibraryPage(UniquePageMixin, Page):
#     template = 'pages/content.html'
#
#     class Meta:
#         verbose_name = _('Media Library')
#
#     parent_page_types = ['cms.HomePage']
#     # subpage_types = ['medialibrary.MediaPage']
#

@register_snippet
class MediaType(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


class Media(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=255,
        unique=True
    )
    abstract = models.TextField(
        _('Abstract'),
    )
    teaser_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Teaser image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    video = models.URLField(
        verbose_name=_('Video'),
        blank=True,
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
    )
    author = models.CharField(
        _('Author'),
        max_length=255,
        blank=True,
    )
    country = CountryField(
        blank=True
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
        FieldPanel('country'),
        StreamFieldPanel('content'),
    ]
