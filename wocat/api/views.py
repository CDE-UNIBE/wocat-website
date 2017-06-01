from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

from rest_framework import status
from rest_framework import viewsets, routers
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from wocat.cms.models import ProjectPage, CountryPage, RegionPage
from wocat.cms.serializers import ProjectPageSerializer, CountryPageSerializer, \
    RegionPageSerializer, CountrySerializer
from wocat.countries.models import Country
from wocat.institutions.models import Institution
from wocat.institutions.serializers import InstitutionSerializer
from wocat.users.models import User
from wocat.users.serializers import UserSerializer

router = routers.DefaultRouter()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
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


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProjectPageSerializer

    def get_queryset(self):
        query_string = self.request.GET.get('q')
        if query_string:
            return ProjectPage.objects.search(query_string)
        else:
            return ProjectPage.objects.all()

router.register(r'projects', ProjectViewSet, base_name='projectpage')


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = CountryPageSerializer

    def get_queryset(self):
        query_string = self.request.GET.get('q')
        if query_string:
            return CountryPage.objects.search(query_string)
        else:
            return CountryPage.objects.all()


router.register(r'countries', CountryViewSet, base_name='countrypage')


class CountryCodeDetailView(RetrieveAPIView):
    """
    Detail view for country code; this approach seems easier than adding to the
    router-urls.
    If no CountryPage exists, the plain Country is returned.
    """
    permission_classes = (AllowAny, )

    def get_serializer_class(self):
        if isinstance(self.get_object(), Country):
            return CountrySerializer
        else:
            return CountryPageSerializer

    def get_object(self):
        try:
            return CountryPage.objects.get(country__code=self.kwargs['country_code'])
        except CountryPage.DoesNotExist:
            return Country.objects.get(code=self.kwargs['country_code'])


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegionPageSerializer

    def get_queryset(self):
        query_string = self.request.GET.get('q')
        if query_string:
            return RegionPage.objects.search(query_string)
        else:
            return RegionPage.objects.all()


router.register(r'regions', RegionViewSet, base_name='regionpage')


class InstitutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


router.register(r'institutions', InstitutionViewSet)


class MapSearchView(TemplateView):
    http_method_names = ['get']
    template_name = 'map/search_results.html'
    filter_elements = ['countries', 'projects', 'regions']

    def prepare_data(self, model_class):
        qs = model_class.objects.live()
        query_string = self.request.GET.get('q')
        if query_string:
            # cast to list, as a searchqueryset (or something...) is returned
            return list(qs.search(query_string))
        return qs

    def get_countries(self):
        return {
            'title': _('Countries'),
            'pages': self.prepare_data(CountryPage)
        }

    def get_projects(self):
        return {
            'title': _('Projects'),
            'pages': self.prepare_data(ProjectPage)
        }

    def get_regions(self):
        return {
            'title': _('Initiatives'),
            'pages': self.prepare_data(RegionPage)
        }

    def get_context_data(self, **kwargs):
        """
        Call the get_<filter> method and put it to the context.
        """
        context = super().get_context_data(**kwargs)
        context.update(
            **getattr(self, 'get_{}'.format(self.kwargs['filter']))()
        )
        return context


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
    throttle_classes = (UserRateThrottle, )

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.data)
        if form.is_valid():
            user = form.get_user()
            return Response(data=UserSerializer(instance=user).data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
