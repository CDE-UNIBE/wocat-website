from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import NewsPage, NewsCountry


class CountryFilter(SimpleListFilter):
    title = _('country')
    parameter_name = 'country'

    def lookups(self, request, model_admin):
        news_countries = NewsCountry.objects.all()
        return [(news_country.id, news_country.country) for news_country in news_countries]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(news_countries=self.value())
            # return queryset.filter(news_countries__=self.value())
        else:
            return queryset


@modeladmin_register
class NewsModelAdmin(ModelAdmin):
    model = NewsPage
    menu_label = _('News')
    menu_icon = 'fa fa-newspaper-o'
    list_display = ('title',)

    search_fields = ('title', 'content')
    list_filter = ('author', 'date', CountryFilter)
