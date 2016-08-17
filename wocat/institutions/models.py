from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class Institution(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        unique=True,
    )
    abbreviation = models.CharField(
        verbose_name=_('Abbreviation'),
        max_length=255,
        unique=True,
    )
    url = models.URLField(
        verbose_name=_('Url'),
        blank=True,
    )
    country = CountryField(
        blank=True
    )
    logo = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Logo'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('abbreviation'),
        FieldPanel('url'),
        FieldPanel('country'),
        ImageChooserPanel('logo'),
    ]

    class Meta:
        verbose_name = _('Institution')
        verbose_name_plural = _('Institutions')

    def __str__(self):
        return self.name
