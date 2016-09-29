from django.db.models import Q
from rest_framework import viewsets, routers

from wocat.cms.models import ProjectPage, CountryPage, RegionPage
from wocat.cms.serializers import ProjectSerializer, CountrySerializer, RegionSerializer
from wocat.institutions.models import Institution
from wocat.institutions.serializers import InstitutionSerializer
from wocat.users.models import User
from wocat.users.serializers import UserSerializer

router = routers.DefaultRouter()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned users by filtering against a
        `name` query parameter in the URL.
        """
        queryset = User.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(
                Q(first_name__contains=name) | Q(last_name__contains=name)
            )
        return queryset


router.register(r'users', UserViewSet, base_name='user')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = ProjectPage.objects.all()
    serializer_class = ProjectSerializer


router.register(r'projects', ProjectViewSet)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = CountryPage.objects.all()
    serializer_class = CountrySerializer


router.register(r'countries', CountryViewSet)


class RegionViewSet(viewsets.ModelViewSet):
    queryset = RegionPage.objects.all()
    serializer_class = RegionSerializer


router.register(r'regions', RegionViewSet)


# class InstitutionViewSet(viewsets.ModelViewSet):
#     queryset = Institution.objects.all()
#     serializer_class = InstitutionSerializer
#
#
# router.register(r'institutions', InstitutionViewSet)
