from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _


class Media(models.Model):
    author = models.CharField(
        _('Author'),
        max_length=255,
        blank=True,
    )
    title = models.CharField(
        _('Title'),
        max_length=255,
    )
    description = models.TextField(
        _('Description'),
        blank=True,
    )
    file = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.PROTECT,
        related_name='+'
    )
    teaser_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    detail_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    country = CountryField(
        blank=True
    )

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')

    def __str__(self):
        return self.title
