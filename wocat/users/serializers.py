from rest_framework import serializers

from wocat.countries.models import Country
from wocat.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    experiences = serializers.StringRelatedField(many=True)
    key_work_topics = serializers.StringRelatedField(many=True)
    country = serializers.PrimaryKeyRelatedField(many=False, queryset=Country.objects.all())
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'pk', 'email', 'first_name', 'last_name', 'gender', 'title',
            'position', 'department', 'function', 'experiences',
            'key_work_topics', 'address', 'address_2', 'postal_code', 'city',
            'country', 'phone', 'phone_2', 'fax', 'fax_2', 'second_email',
            'language', 'comments', 'newsletter', 'avatar', 'institution',
            'full_name', 'is_active',
        ]

    def get_full_name(self, obj):
        return obj.get_full_name()
