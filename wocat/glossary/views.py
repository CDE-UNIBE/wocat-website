from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Entry


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'glossary/entry.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class EntryListView(ListView):
    model = Entry
    template_name = 'glossary/list.html'
    context_object_name = 'entries'
