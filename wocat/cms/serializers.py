from rest_framework import serializers

from wocat.cms.models import ProjectPage, CountryPage, RegionPage


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='full_url')
    countries = serializers.StringRelatedField(many=True)

    class Meta:
        model = ProjectPage
        fields = ['url', 'title', 'countries', 'contact_person']


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='full_url')
    code = serializers.CharField(source='country.code')

    class Meta:
        model = CountryPage
        fields = ['url', 'title', 'code', 'contact_person']


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='full_url')
    countries = serializers.StringRelatedField(many=True)

    class Meta:
        model = RegionPage
        fields = ['url', 'title', 'countries', 'country_codes', 'contact_person']
