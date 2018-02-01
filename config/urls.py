# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import RedirectView
from wagtail.contrib.wagtailsitemaps.views import sitemap

from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls

from wocat.cms.views import AddLanguagePrefixRedirectView
from wocat.core.views import SwitchLanguageView
from wocat.users.views import ReactivateAccountView

BACKEND_NAME = 'WOCAT backend'
admin.site.site_header = BACKEND_NAME
admin.site.site_title = BACKEND_NAME

urlpatterns = [
    url('^sitemap\.xml$', sitemap),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^{}/'.format(settings.ADMIN_URL), include(admin.site.urls)),

    # User management
    url(r'^users/', include('wocat.users.urls', namespace='users')),
    url(r"^accounts/reactivate/$", ReactivateAccountView.as_view(), name="reactivate_account"),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^library/media/', include('wocat.medialibrary.urls', namespace='media')),
    # Redirect requests to fileadmin/* (old document folder) to new media library
    url(r'^fileadmin/', RedirectView.as_view(url='/en/wocat-media-library')),
    url(r'^glossary/', include('wocat.glossary.urls', namespace='glossary')),
    url(r'^institutions/', include('wocat.institutions.urls', namespace='institutions')),
    url(r'^countries/', include('wocat.countries.urls', namespace='countries')),
    url(r'^search/', include('wocat.search.urls', namespace='search')),
    url(r'^cmsviews/', include('wocat.cms.urls', namespace='cms')),
    url(r'^newsletter/', include('wocat.newsletter.urls', namespace='newsletter')),

    # Your stuff: custom urls includes go here

    url(r'^i18n/$', SwitchLanguageView.as_view(), name='set_language'),
]
# Static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
        url(r'^styleguide/', include("wocat.styleguide.urls", namespace="styleguide")),
    ]

    # debug-toolbar
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += [
    url(r'^api/', include('wocat.api.urls'))
]

urlpatterns += [
    # Users should not be deleted! Manually catching requests to delete users
    # in the CMS and showing them a message.
    url(
        regex=r'^cms/users/(?P<pk>\d+)/delete/$',
        view=TemplateView.as_view(template_name='users/confirm_delete.html'),
        name='cms_user_delete'
    ),
    # CMS
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^(?!({})|static|media)(.+)'.format('|'.join([l[0] for l in settings.LANGUAGES])), AddLanguagePrefixRedirectView.as_view()),
    url(r'^', include(wagtail_urls)),
]
