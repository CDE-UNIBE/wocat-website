# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from wocat.api.views import router
from . import views


v1_urlpatterns = [
    # URL pattern for the UserListView
    url(r'^', include(router.urls)),
    url(r'^auth/login/$', views.LoginView().as_view()),
    url(r'docs/$', get_swagger_view(title='Wocat API'))
]

urlpatterns = [
    # URL pattern for the UserListView
    url(r'^v1/', include(v1_urlpatterns)),
]
