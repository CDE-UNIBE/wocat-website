# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import NewsletterManagementView

urlpatterns = [
    url(
        regex=r'^management/$',
        view=NewsletterManagementView.as_view(),
        name='index'
    ),
]
