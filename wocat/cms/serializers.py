import json
from functools import lru_cache

from django.conf import settings
from django.core.cache import cache

from rest_framework import serializers

from wocat.cms.models import ProjectPage, CountryPage, RegionPage


class GeoJsonMixin:
    """
    Shared methods for all things geojson.
    """
    filename = 'countries.geo.json'  # todo: move to settings.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geojson, self.country_keys = self.load_geojson()

    @lru_cache(maxsize=32)
    def get_country_geojson(self, country: str) -> dict:
        if country in self.country_keys:
            return self.geojson['features'][self.country_keys[country]]
        # else what? log error and display in template? how is logging handled?

    def load_geojson(self) -> tuple:
        """
        Get a tuple of two elements:
        - python object of the defined geojson file
        - dict with all countries and their list index for easy access
        The object is collected from the cache, with the filename as cache key.
        Therefore, the date should be appended to the filename as version
        identifier.
        """
        geojson, country_keys = cache.get(self.filename, (None, None))
        if not geojson:
            path = '{}/wocat/static/js/{}'.format(settings.ROOT_DIR, self.filename)
            with open(path) as geojson_file:
                geojson = json.loads(geojson_file.read())
                # Provide helper dict to easily access countries.
                country_keys = {item['id']: index for index, item in enumerate(geojson['features'])}
                cache.set(self.filename, (geojson, country_keys))
        return geojson, country_keys

    def get_geojson(self, obj) -> list:
        raise NotImplementedError('The field "geojson" is required (frontend).')


class ProjectSerializer(GeoJsonMixin, serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='full_url')
    geojson = serializers.SerializerMethodField()

    class Meta:
        model = ProjectPage
        fields = ('url', 'title', 'geojson')

    def get_geojson(self, obj: ProjectPage) -> list:
        countries = ['ALB', 'DEU', 'CAN']
        return [self.get_country_geojson(country) for country in countries]


class CountrySerializer(GeoJsonMixin, serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='full_url')
    code = serializers.CharField(source='country.code')
    geojson = serializers.SerializerMethodField()

    class Meta:
        model = CountryPage
        fields = ('url', 'title', 'code', 'geojson')

    def get_geojson(self, obj: CountryPage) -> list:
        return self.get_country_geojson(obj.country.code)


class RegionSerializer(GeoJsonMixin, serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='full_url')
    geojson = serializers.SerializerMethodField()

    class Meta:
        model = RegionPage
        fields = ('url', 'title', 'country_codes', 'geojson')

    def get_geojson(self, obj: RegionPage) -> list:
        countries = ['ARG', 'ARM']
        return [self.get_country_geojson(country) for country in countries]
