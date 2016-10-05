from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import NewsPage


@modeladmin_register
class NewsModelAdmin(ModelAdmin):
    model = NewsPage
    menu_label = _('News')
    menu_icon = 'fa fa-newspaper-o'
    list_display = ('title',)

    search_fields = ('title', 'content')
    list_filter = ('author', 'date', 'country')
