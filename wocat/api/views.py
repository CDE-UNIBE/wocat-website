from rest_framework import viewsets, routers

from wocat.institutions.models import Institution
from wocat.institutions.serializers import InstitutionSerializer
from wocat.users.models import User
from wocat.users.serializers import UserSerializer

router = routers.DefaultRouter()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router.register(r'users', UserViewSet)


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


router.register(r'institutions', InstitutionViewSet)
