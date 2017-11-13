from rest_framework import serializers

from wocat.countries.models import Country
from wocat.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.SerializerMethodField()
    country = serializers.PrimaryKeyRelatedField(many=False, queryset=Country.objects.all())
    country_name = serializers.SerializerMethodField()
    experiences = serializers.StringRelatedField(many=True)
    full_name = serializers.SerializerMethodField()
    institution_name = serializers.SerializerMethodField()
    institution_url = serializers.SerializerMethodField()
    key_work_topics = serializers.StringRelatedField(many=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'address', 'address_2', 'avatar', 'avatar', 'city', 'comments',
            'country', 'country_name', 'department', 'email', 'experiences',
            'fax', 'fax_2', 'first_name', 'full_name', 'function', 'gender',
            'institution', 'institution_name', 'institution_url', 'is_active',
            'key_work_topics', 'language', 'last_name', 'newsletter', 'phone',
            'phone_2', 'pk', 'position', 'postal_code', 'second_email', 'title',
            'url'
        ]

    def get_full_name(self, obj):
        return obj.get_full_name()

    def get_avatar(self, obj):
        return obj.avatar['avatarsquare'].url if obj.avatar else ''

    def get_country_name(self, obj):
        return obj.country.name if obj.country else ''

    def get_institution_name(self, obj):
        return obj.institution.name if obj.institution else ''

    def get_institution_url(self, obj):
        return obj.institution.url if obj.institution else ''

    def get_url(self, obj):
        return obj.get_absolute_url()
