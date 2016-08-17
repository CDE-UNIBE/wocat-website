# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include

from wocat.api.views import router
from . import views

v1_urlpatterns = [
    # URL pattern for the UserListView
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls')),
]

urlpatterns = [
    # URL pattern for the UserListView
    url(r'^v1/', include(v1_urlpatterns)),
]
