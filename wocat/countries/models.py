from autoslug import AutoSlugField
from django.urls import reverse, reverse_lazy
from django.db import models
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _
from django_countries import countries
from wagtail.wagtailsnippets.models import register_snippet


# @register_snippet
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
        verbose_name_plural = _('Countries')
        ordering = ['name']

    def __str__(self):
        # Use translations of django-countries
        country_alpha2 = countries.alpha2(self.code)
        return dict(countries)[country_alpha2]

    def get_absolute_url(self):
        return reverse('countries:detail', args=[self.slug])

    @property
    def flag(self):
        code = self.code
        if code:
            return static('countries/flags/flags/png/{code}.png'.format(code=self.code.lower()))
        else:
            return ''

    def get_api_detail_url(self):
        return '{url}?country_code={code}'.format(
            url=reverse_lazy('country-detail'),
            code=self.code
        )


@register_snippet
class Continent(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True,
    )

    slug = AutoSlugField(
        populate_from='name'
    )

    class Meta:
        verbose_name = _('Continent')
        verbose_name_plural = _('Continents')
        ordering = ['name']

    def __str__(self):
        return self.name
