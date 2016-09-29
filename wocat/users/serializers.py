from rest_framework import serializers

from wocat.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'is_staff', 'first_name', 'last_name')
