from rest_framework import serializers

from wocat.institutions.models import Institution


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='institution-detail')
    external_url = serializers.URLField(source='url')

    class Meta:
        model = Institution
        fields = ('url', 'external_url', 'name', 'abbreviation')
