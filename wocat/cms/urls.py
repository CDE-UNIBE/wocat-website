# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import DocumentUploadView, DocumentUploadDeleteView

urlpatterns = [
    url(
        regex=r'^upload/(?P<page_pk>[0-9]+)/(?P<module_id>[0-9]+)/(?P<upload_slug>[-\w]+)/$',
        view=DocumentUploadView.as_view(),
        name='upload'
    ),
    url(
        regex=r'^upload-delete/(?P<document_id>[0-9]+)/$',
        view=DocumentUploadDeleteView.as_view(),
        name='upload-delete'
    ),
    # url(
    #     regex=r'^(?P<slug>[\w.@+-]+)/$',
    #     view=CountryDetailView.as_view(),
    #     name='detail'
    # ),
]
