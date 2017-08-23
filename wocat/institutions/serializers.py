from rest_framework import serializers

from wocat.institutions.models import Institution


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='institutions:detail', lookup_field='slug')
    external_url = serializers.URLField(source='url')
    # country = serializers.URLField(source='country.get_absolute_url')
    # country = serializers.PrimaryKeyRelatedField(
    #     many=False,
    #     # lookup_field='code'
    # )
    # country = serializers.HyperlinkedRelatedField(
    #     view_name='countries:detail',
    #     lookup_field='slug',
    #     read_only=True
    # )

    country = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Institution
        fields = [
            'id', 'url', 'external_url', 'name', 'abbreviation', 'year', 'country', 'contact_person', 'memorandum'
        ]
