# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import InstitutionDetailView, InstitutionListView

urlpatterns = [
    url(
        regex=r'^$',
        view=InstitutionListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=InstitutionDetailView.as_view(),
        name='detail'
    ),
]
