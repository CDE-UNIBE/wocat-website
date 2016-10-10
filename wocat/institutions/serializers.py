from rest_framework import serializers

from wocat.institutions.models import Institution


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='institutions:detail')
    external_url = serializers.URLField(source='url')
    country = serializers.URLField(source='country.get_absolute_url')

    class Meta:
        model = Institution
        fields = ('url', 'external_url', 'name', 'abbreviation', 'year', 'country', 'contact_person', 'memorandum')
