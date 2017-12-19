from urllib.parse import urlparse

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.translation import LANGUAGE_SESSION_KEY, check_for_language, \
    get_language
from django.views.generic import RedirectView
from wagtail.wagtailcore.models import Page

from wocat.cms.models import TranslatablePageMixin


class SwitchLanguageView(RedirectView):
    """
    POST to this view to switch the language. Tries to find page content in the
    new language and shows it or falls back to content in default language if no
    translation available.
    """
    permanent = False
    original_lang_code = 'en'

    @staticmethod
    def rreplace(s: str, old: str, new: str, occurrence: int) -> str:
        """Helper function to replace a string from the end."""
        li = s.rsplit(old, occurrence)
        return new.join(li)

    @staticmethod
    def set_language(
            request: WSGIRequest, response: HttpResponse, lang_code: str):
        """Set the language as session or cookie."""
        if hasattr(request, 'session'):
            request.session[LANGUAGE_SESSION_KEY] = lang_code
        else:
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME, lang_code,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
            )

    def get_url_path(self, request: WSGIRequest, url: str):
        """Extract the url_path (as in the DB) of the url."""
        prefix = request.site.root_page.url_path
        next_url_parsed = urlparse(url)
        if prefix.endswith('/'):
            prefix = self.rreplace(prefix, '/', '', 1)
        url_path = '{}{}'.format(prefix, next_url_parsed.path)
        if not url_path.endswith('/'):
            url_path = '{}/'.format(url_path)
        return url_path

    def post(self, request, *args, **kwargs):
        next_url = request.POST.get('next')
        if not next_url:
            next_url = request.META.get('HTTP_REFERER')

        curr_lang_code = get_language()
        new_lang_code = request.POST.get('language')
        if not check_for_language(new_lang_code):
            # Language is not valid, simply redirect
            return redirect(next_url)

        if curr_lang_code == new_lang_code:
            # No need to look up Pages if language did not change
            return redirect(next_url)

        url_path = self.get_url_path(request, next_url)

        # Get the Page object to redirect to in the current language
        try:
            page = Page.objects.in_site(request.site).live().get(
                url_path=url_path).specific
        except Page.DoesNotExist:
            # If no CMS page exists (e.g. login page), switch the language and
            # redirect.
            response = redirect(next_url)
            self.set_language(request, response, new_lang_code)
            return response

        if curr_lang_code == self.original_lang_code:
            # If the current language is the original (en), then check if there
            # is a translation in the new language. If not, the original is
            # served.
            new_page = TranslatablePageMixin.get_translated_page(
                page, new_lang_code)
            response = redirect(new_page.url)
        else:
            # If the current language is a translation ...
            original_page = page.original_page()
            if new_lang_code == self.original_lang_code:
                # ... and the new language is the original (en), then return the
                # original
                response = redirect(original_page.url)
            else:
                # ... and the new language is also a translation, get the
                # original (en) and try to return a translation in the new
                # language. If not available, return the original
                new_page = TranslatablePageMixin.get_translated_page(
                    page, new_lang_code)
                response = redirect(new_page.url)

        # Actually set the new language and return the response
        self.set_language(request, response, new_lang_code)
        return response
