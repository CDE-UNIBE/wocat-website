from autoslug import AutoSlugField
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from django.core.validators import MaxValueValidator

from wocat.countries.models import Country


class Institution(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
    )
    slug = AutoSlugField(
        populate_from='name'
    )
    abbreviation = models.CharField(
        verbose_name=_('Abbreviation'),
        max_length=255,
    )
    url = models.URLField(
        verbose_name=_('Url'),
        blank=True,
    )
    year = models.PositiveIntegerField(
        _('Year'),
        default=timezone.now().year,
        validators=[MaxValueValidator(4000)]
    )
    country = models.ForeignKey(
        Country,
        blank=True, null=True,
        on_delete=models.PROTECT,
    )
    contact_person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='institution_contact',
        verbose_name=_('Contact person'),
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    memorandum = models.BooleanField(
        verbose_name=_('Memorandum signed'),
        default=False
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
        # FieldPanel('slug'),
        FieldPanel('abbreviation'),
        FieldPanel('url'),
        FieldPanel('year'),
        FieldPanel('country'),
        FieldPanel('contact_person'),
        FieldPanel('memorandum'),
        ImageChooserPanel('logo'),
    ]

    search_fields = [
        index.SearchField('name'),
        index.SearchField('abbreviation'),
        index.SearchField('content'),
        index.FilterField('year'),
        index.FilterField('contact_person'),
        index.FilterField('country'),
    ]

    class Meta:
        verbose_name = _('Institution')
        verbose_name_plural = _('Institutions')
        ordering = ['name']
        unique_together = ('name', 'abbreviation', 'country')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('institutions:detail', args=[self.slug])
