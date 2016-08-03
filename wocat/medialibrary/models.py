from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from wocat.core.blocks import CORE_BLOCKS


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
        on_delete=models.PROTECT,
        related_name='+'
    )
    author = models.CharField(
        _('Author'),
        max_length=255,
        blank=True,
    )
    country = CountryField(
        blank=True
    )
    # TYPE_1 = 1
    # TYPE_2 = 2
    # TYPE_3 = 3
    # MEDIA_TYPE_CHOICES = (
    #     (TYPE_1, _('Type 1')),
    #     (TYPE_2, _('Type 2')),
    #     (TYPE_3, _('Type 3')),
    # )
    # media_type = models.PositiveSmallIntegerField(
    #     verbose_name=_('Type'),
    #     choices=MEDIA_TYPE_CHOICES,
    #     blank=True, null=True,
    # )
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
