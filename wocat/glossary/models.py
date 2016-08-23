from autoslug import AutoSlugField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class Entry(models.Model):
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
