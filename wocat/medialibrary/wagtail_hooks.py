from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel

from .models import Media


@modeladmin_register
class MediaModelAdmin(ModelAdmin):
    model = Media
    menu_label = _('Media Library')
    menu_icon = 'fa fa-file-o'
    list_display = ('author', 'title', 'country')

    list_filter = ('author',)
    search_fields = ('title',)
