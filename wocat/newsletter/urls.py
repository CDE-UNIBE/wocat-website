# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import NewsletterManagementView, NewsletterUnsubscribeView

urlpatterns = [
    url(
        regex=r'^management/$',
        view=NewsletterManagementView.as_view(),
        name='index'
    ),
    url(
        regex=r'^unsubscribe/$',
        view=NewsletterUnsubscribeView.as_view(),
        name='unsubscribe'
    ),
]
