import django_filters

from .models import Media


class MediaFilter(django_filters.FilterSet):
    class Meta:
        model = Media
        fields = ['media_type', 'country', 'continent']
