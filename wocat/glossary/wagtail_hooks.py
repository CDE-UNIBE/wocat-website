from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Entry


@modeladmin_register
class EntryModelAdmin(ModelAdmin):
    model = Entry
    menu_label = _('Glossary')
    menu_icon = 'fa fa-book'
    list_display = ('title',)
    list_filter = ('acronym',)
    search_fields = ('title', 'description')
