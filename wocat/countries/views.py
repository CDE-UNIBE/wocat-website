from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Country


class CountryDetailView(DetailView):
    model = Country
    template_name = 'countries/detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class CountryListView(ListView):
    model = Country
    template_name = 'countries/list.html'
    context_object_name = 'countries'
