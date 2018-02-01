from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import StyleguideView

urlpatterns = [
    url(r'^$', StyleguideView.as_view(), name='styleguide'),
    url(r'^demos/(?P<template>.*)/$', StyleguideView.as_view(), name='styleguide'),
]
