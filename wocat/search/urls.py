# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import SearchView

urlpatterns = [
    url(
        regex=r'^$',
        view=SearchView.as_view(),
        name='index'
    ),
]
