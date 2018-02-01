from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Media


class MediaDetailView(DetailView):
    model = Media
    template_name = 'medialibrary/media.html'
