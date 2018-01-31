from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):
    code = models.CharField(
        verbose_name='language code',
        max_length=3,
        unique=True,
    )

    name = models.CharField(
        verbose_name='name',
        max_length=255,
        unique=True,
    )

    slug = AutoSlugField(
        populate_from='name'
    )

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')
        ordering = ['name']

    def __str__(self):
        return self.name
