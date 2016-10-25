from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import Institution


@modeladmin_register
class InstitutionModelAdmin(ModelAdmin):
    model = Institution
    menu_label = _('Institution')
    menu_icon = 'fa fa-institution'
    list_display = ('name', 'abbreviation', 'year', 'country', 'contact_person', 'logo_html', 'memorandum')

    search_fields = ('name',)

    def logo_html(self, obj):
        html = '-'
        url = obj.logo.get_rendition('max-40x40').url if obj.logo else ''
        if url:
            html = format_html('<img src="{}">', url)
        return html

    logo_html.short_description = _('Logo')
