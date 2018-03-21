# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import DocumentUploadView, DocumentUploadDeleteView

urlpatterns = [
    url(
        regex=r'^upload/(?P<page_pk>[\d]+)/(?P<module_id>[\d]+)/$',
        view=DocumentUploadView.as_view(),
        name='upload'
    ),
    url(
        regex=r'^upload-delete/(?P<document_id>[\d]+)/$',
        view=DocumentUploadDeleteView.as_view(),
        name='upload-delete'
    ),
]
