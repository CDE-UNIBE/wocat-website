from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet


# @register_snippet
class Institution(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        unique=True,
    )

    panels = [
        FieldPanel('name'),
    ]

    class Meta:
        verbose_name = _('Institution')
        verbose_name_plural = _('Institutions')

    def __str__(self):
        return self.name
