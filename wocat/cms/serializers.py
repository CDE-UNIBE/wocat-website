import collections
from functools import lru_cache
import json

import itertools
from django.conf import settings
from django.core.cache import cache
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from wocat.cms.models import ProjectPage, CountryPage, RegionPage
from wocat.countries.models import Country

Descendant = collections.namedtuple('Descendant', ['name', 'url', 'type'])


class GeoJsonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Shared methods for all things geojson.
    """
    filename = settings.MAP_GEOJSON_FILE
    geojson = serializers.SerializerMethodField()
    panel_text = serializers.SerializerMethodField()
    identifier = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geojson, self.country_keys = self.load_geojson()

    @lru_cache(maxsize=32)
    def get_country_geojson(self, country: str) -> dict:
        if country in self.country_keys:
            return self.geojson['features'][self.country_keys[country]]
        raise ValueError('%s not in geojson' % country)

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
        raise NotImplementedError('The field "geojson" is required.')

    def get_descendants(self, obj) -> list:
        raise NotImplemented('The method "get_descendants" is required.')

    def _descendant(self, country):
        yield Descendant(
            name=country.__str__(),
            type='countries',
            #url=reverse_lazy('country-detail', kwargs={'country_code': str(country.pk)})
            url='/api/v1/country-detail/{}/'.format(country.pk)
        )

    def get_panel_text(self, obj) -> str:
        """
        Get the text on display in the right panel.
        """
        image = ''
        if obj.header_images:
            try:
                image = obj.header_images[0].value.get_rendition('max-500x500').url
            except OSError:
                # Simply show no image in case of problems with the files.
                image = ''
        return render_to_string('api/partial/panel_text.html', {
            'identifier': self.get_identifier(obj),
            'title': obj.title,
            'lead': obj.lead,
            'url': obj.url,
            'image': image,
            'descendants_title': self.descendants_title,
            'descendants': self.get_descendants(obj),
        })

    def get_identifier(self, obj) -> str:
        """
        Get a unique identifier for this element. Used to highlight the item in
        the frontend.
        """
        return '{label}-{id}'.format(label=self.Meta.model.__name__.lower(), id=obj.id)


class ProjectPageSerializer(GeoJsonSerializer):

    class Meta:
        model = ProjectPage
        fields = ('identifier', 'geojson', 'panel_text', )

    def get_countries(self, obj):
        return set(itertools.chain(
            obj.countries, obj.included_countries.all())
        )

    def get_geojson(self, obj: ProjectPage) -> list:
        countries = self.get_countries(obj) or []
        return [self.get_country_geojson(country.code) for country in countries]

    @property
    def descendants_title(self):
        return _('Included countries')

    def get_descendants(self, obj):
        for country in self.get_countries(obj):
            yield from self._descendant(country)


class CountryPageSerializer(GeoJsonSerializer):

    class Meta:
        model = CountryPage
        fields = ('identifier', 'geojson', 'panel_text',)

    def get_geojson(self, obj: CountryPage):
        return self.get_country_geojson(obj.country.code)

    @property
    def descendants_title(self):
        return _('Included projects')

    def get_descendants(self, obj):
        return []


class CountrySerializer(GeoJsonSerializer):

    def get_geojson(self, obj: Country):
        return self.get_country_geojson(obj.code)

    @property
    def descendants_title(self):
        return ''

    def get_descendants(self, obj):
        return []

    def get_panel_text(self, obj) -> str:
        return render_to_string('api/partial/panel_text.html', {
            'title': obj.name
        })

    class Meta:
        model = Country
        fields = ('geojson', 'panel_text')


class RegionPageSerializer(GeoJsonSerializer):

    class Meta:
        model = RegionPage
        fields = ('identifier', 'geojson', 'panel_text', )

    def get_geojson(self, obj: RegionPage) -> list:
        return [self.get_country_geojson(code) for code in obj.country_codes]

    @property
    def descendants_title(self):
        return _('Included countries')

    def get_descendants(self, obj):
        for country in obj.countries:
            yield from self._descendant(country.country)
