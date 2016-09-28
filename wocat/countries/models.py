from django.db import models
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

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Coutries')
        ordering = ['name']

    def __str__(self):
        return self.name
