# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import CountryDetailView, CountryListView

urlpatterns = [
    url(
        regex=r'^$',
        view=CountryListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=CountryDetailView.as_view(),
        name='detail'
    ),
]
