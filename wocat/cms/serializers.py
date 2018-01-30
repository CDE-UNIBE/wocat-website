import collections
from django.db.models import Q
from django.utils import translation
from functools import lru_cache
import json

import itertools
from django.conf import settings
from django.core.cache import cache
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from wocat.cms.models import ProjectPage, RegionPage, ProjectCountryPage, \
    CountryPage, TranslatablePageMixin
from wocat.countries.models import Country


Descendant = collections.namedtuple('Descendant', ['name', 'url'])
CountryDescendant = collections.namedtuple(
    'CountryDescendant', ['name', 'url', 'countrypage_url', 'project']
)


class GeoJsonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Shared methods for all things geojson.
    """
    filename = settings.MAP_GEOJSON_FILE
    geojson = serializers.SerializerMethodField()
    panel_text = serializers.SerializerMethodField()

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

    def _descendant_country(self, country):
        yield Descendant(
            name=country.__str__(),
            url=country.get_api_detail_url()
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
            'title': obj.title,
            'lead': obj.lead,
            'url': obj.url,
            'image': image,
            'descendants_title': self.descendants_title,
            'descendants': self.get_descendants(obj),
        })


class ProjectPageSerializer(GeoJsonSerializer):

    class Meta:
        model = ProjectPage
        fields = ('geojson', 'panel_text', )

    def get_countries(self, obj):
        return set(itertools.chain(
            [country_page.country for country_page in obj.countries],
            obj.included_countries.all())
        )

    def get_geojson(self, obj: ProjectPage) -> list:
        countries = self.get_countries(obj) or []
        return [self.get_country_geojson(country.code) for country in countries]

    @property
    def descendants_title(self):
        return _('Included countries')

    def get_descendants(self, obj):
        for country in self.get_countries(obj):
            yield from self._descendant_country(country)


class CountrySerializer(GeoJsonSerializer):
    """
    Not all countries have a countrypage, therefore references through
    ProjectPage.included_countries and ProjectPage - ProjectCountriesPage -
    ProjectCountry are resolved.
    """

    def get_geojson(self, obj: Country):
        return self.get_country_geojson(obj.code)

    @property
    def descendants_title(self):
        return _('Projects')

    def get_current_language(self):
        return translation.get_language_from_request(
            self.context['request'])

    def get_descendants(self, obj):
        project_country_pages = ProjectCountryPage.objects.filter(country=obj)
        for project in project_country_pages:
            yield CountryDescendant(
                name=project.get_parent().get_parent().title,
                url=reverse('projectpage-detail', kwargs={
                    'pk': project.get_parent().get_parent().pk
                }),
                countrypage_url=project.url,
                project=project.title
            )

        included_projects = ProjectPage.objects.filter(included_countries=obj)

        current_language = self.get_current_language()
        if current_language == TranslatablePageMixin.original_lang_code:
            # If the current language is the original, limit results to only
            # these (identified by url_path)
            included_projects = included_projects.filter(
                url_path__startswith='/home/{}/'.format(current_language))
        else:
            # If a translation language is currently active, query all original
            # pages and the translations in the current language. Then exclude
            # all original pages with translations in the current language
            # (having a link to the translation)
            included_projects = included_projects.filter(
                Q(url_path__startswith='/home/{}/'.format(current_language)) |
                Q(url_path__startswith='/home/{}/'.format(
                    TranslatablePageMixin.original_lang_code))).exclude(
                **{'{}_link__isnull'.format(current_language): False})

        for project in included_projects:
            yield Descendant(
                name=project.title,
                url=reverse('projectpage-detail', kwargs={'pk': project.pk}),
            )

    def get_country_page(self, obj):
        language = self.get_current_language()
        original_country_page = ''
        translated_country_page = ''
        country_pages = CountryPage.objects.filter(country=obj)
        for page in country_pages:
            if page.is_original:
                original_country_page = page
            if language == page.get_language():
                translated_country_page = page
        return translated_country_page or original_country_page

    def get_panel_text(self, obj) -> str:
        country_page = self.get_country_page(obj)
        title = country_page.title if country_page is not None else obj.name
        return render_to_string('api/partial/panel_text.html', {
            'title': title,
            'descendants_title': self.descendants_title,
            'descendants': self.get_descendants(obj),
            'image': obj.flag,
            'country_page': country_page,
        })

    class Meta:
        model = Country
        fields = ('geojson', 'panel_text', )


class RegionPageSerializer(GeoJsonSerializer):

    class Meta:
        model = RegionPage
        fields = ('geojson', 'panel_text', )

    def get_geojson(self, obj: RegionPage) -> list:
        return [self.get_country_geojson(code) for code in obj.country_codes]

    @property
    def descendants_title(self):
        return _('Included countries')

    def get_descendants(self, obj):
        for country in obj.countries:
            yield from self._descendant_country(country.country)
