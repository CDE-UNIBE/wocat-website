from autoslug import AutoSlugField
from django.core.urlresolvers import reverse
from django.db import models
from django.templatetags.static import static
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    code = models.CharField(
        verbose_name=_('code (alpha3)'),
        max_length=3,
        primary_key=True,
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True,
    )
    slug = AutoSlugField(
        populate_from='name'
    )

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Coutries')
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('countries:detail', args=[self.slug])

    @property
    def flag(self):
        return static('countries/flags/flags/png/{code}.png'.format(code=self.code))
