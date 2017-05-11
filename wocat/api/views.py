from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from rest_framework import status
from rest_framework import viewsets, routers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from wocat.cms.models import ProjectPage, CountryPage, RegionPage
from wocat.cms.serializers import ProjectSerializer, CountrySerializer, RegionSerializer
from wocat.institutions.models import Institution
from wocat.institutions.serializers import InstitutionSerializer
from wocat.users.models import User
from wocat.users.serializers import UserSerializer

router = routers.DefaultRouter()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """
        Optionally restricts the returned users by filtering against a
        `name` query parameter in the URL.
        """
        queryset = User.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
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


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


router.register(r'institutions', InstitutionViewSet)


class LoginView(APIView):
    """
    Endpoint for authentication, expects username and password in the request
    body.

    Selected response messages:
    * 200 (User object as response)
    * 403 (Forbidden; Token in the request header not valid)
    * 401 (Login failed for given user and password)

    Example request:

    `curl -X POST https://beta.wocat.net/api/v1/auth/login/ \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Token <token>' \
    -d '{"username": "<email>", "password": "<password>"}'`

    """
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.data)
        if form.is_valid():
            user = form.get_user()
            return Response(data=UserSerializer(instance=user).data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
