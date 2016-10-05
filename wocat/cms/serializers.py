from rest_framework import serializers

from wocat.cms.models import ProjectPage, CountryPage, RegionPage


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='full_url')

    class Meta:
        model = ProjectPage
        fields = ('url', 'title')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='full_url')
    code = serializers.CharField(source='country.code')

    class Meta:
        model = CountryPage
        fields = ('url', 'title', 'code')


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='full_url')

    class Meta:
        model = RegionPage
        fields = ('url', 'title', 'country_codes')
