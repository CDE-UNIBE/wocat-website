from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Institution


class InstitutionDetailView(DetailView):
    model = Institution
    template_name = 'institutions/detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class InstitutionListView(ListView):
    model = Institution
    template_name = 'institutions/list.html'
    context_object_name = 'institutions'
