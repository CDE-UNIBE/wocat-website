from rest_framework import serializers

from wocat.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    experiences = serializers.StringRelatedField(many=True)
    key_work_topics = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = [
            'pk',
            'first_name', 'last_name', 'gender', 'title', 'position', 'department', 'function', 'experiences',
            'key_work_topics', 'address', 'address_2', 'postal_code', 'city', 'country', 'phone', 'phone_2',
            'fax', 'fax_2', 'second_email', 'language', 'comments', 'newsletter', 'avatar', 'institution',
            'date_joined', 'is_active', 'is_staff',
        ]
