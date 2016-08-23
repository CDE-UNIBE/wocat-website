# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import EntryDetailView, EntryListView

urlpatterns = [
    url(
        regex=r'^list/$',
        view=EntryListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=EntryDetailView.as_view(),
        name='detail'
    ),
]
