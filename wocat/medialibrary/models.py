from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _


class Media(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(
        _('Title'),
        max_length=255,
    )
    file = models.ForeignKey(
        'wagtaildocs.Document',
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
