from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import Institution


@modeladmin_register
class InstitutionModelAdmin(ModelAdmin):
    model = Institution
    menu_label = _('Institution')
    menu_icon = 'fa fa-institution'
    list_display = ('name',)

    search_fields = ('name',)
