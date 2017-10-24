from django.contrib.auth.models import AnonymousUser
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from rest_framework import authentication, exceptions


class SameHostAjaxAuthentication(authentication.BaseAuthentication):
    """
    Not really an authenticator - allow ajax requests from the current domain.
    """
    def authenticate(self, request):
        current_site = Site.objects.get_current()
        is_same_domain = current_site.domain == request._request.META['HTTP_HOST']
        if request._request.is_ajax() and is_same_domain:
            return (AnonymousUser, None)
        else:
            raise exceptions.AuthenticationFailed(_('Invalid host.'))
