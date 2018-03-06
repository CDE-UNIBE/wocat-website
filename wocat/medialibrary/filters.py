import django_filters
from django.db.models import Min, Max, Q
from django.forms import TextInput
from django.utils.translation import ugettext_lazy as _

from wocat.countries.models import Country
from wocat.languages.models import Language
from .models import Media


def get_media_years_choices():
    """
    Return a range of year integers as tuples from minimum to maximum year
    available in the DB.
    """
    min_max_query = Media.objects.all().aggregate(Min('year'), Max('year'))
    for y in range(min_max_query['year__min'], min_max_query['year__max'] + 1):
        yield (y, y)


def get_media_type_choices():
    """
    Filter the list of choices, return only the ones used.
    """
    used_media_types = Media.objects.values_list(
        'media_type', flat=True).distinct()
    return [
        choice for choice in Media.MEDIA_TYPES if choice[0] in used_media_types]


class MediaLibraryFilter(django_filters.FilterSet):
    # Store years to query DB only once
    media_year_choices = list(reversed(list(get_media_years_choices())))

    media_type = django_filters.ChoiceFilter(
        name='media_type', choices=get_media_type_choices(),
        empty_label=_('All types'), label='')
    search = django_filters.CharFilter(
        method='media_search',
        widget=TextInput(attrs={'placeholder': _('Search')}), label='')
    languages = django_filters.ModelChoiceFilter(
        name='languages',
        queryset=Language.objects.filter(media__isnull=False).distinct(),
        empty_label=_('All languages'), label='')
    year__gte = django_filters.ChoiceFilter(
        name='year', choices=media_year_choices, lookup_expr='gte',
        empty_label=_('Since (all years)'), label='')
    year__lte = django_filters.ChoiceFilter(
        name='year', choices=media_year_choices, lookup_expr='lte',
        empty_label=_('Until (all years)'), label='')
    countries = django_filters.ModelChoiceFilter(
        name='countries',
        queryset=Country.objects.filter(media__isnull=False).distinct(),
        empty_label=_('All countries'), label='')

    class Meta:
        model = Media
        fields = ['continent']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['continent'].extra['empty_label'] = _('All continents')
        self.filters['continent'].label = ''

    def media_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(abstract__icontains=value) |
            Q(author__icontains=value) | Q(content__icontains=value))
