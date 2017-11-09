from rest_framework import serializers

from wocat.institutions.models import Institution


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='institutions:detail', lookup_field='slug')
    external_url = serializers.URLField(source='url')
    country = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    country_name = serializers.SerializerMethodField()
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Institution
        fields = [
            'id', 'url', 'external_url', 'name', 'abbreviation', 'year',
            'country', 'country_name', 'contact_person', 'memorandum', 'logo'
        ]

    def get_logo(self, obj):
        if obj.logo and 'request' in self.context:
            img_path = obj.logo.get_rendition('max-320x320').url
            return self.context['request'].build_absolute_uri(img_path)
        return ''

    def get_country_name(self, obj):
        return obj.country.name if obj.country else ''
