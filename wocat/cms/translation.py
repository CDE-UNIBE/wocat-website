from django.conf import settings
from django.db import models
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.templatetags.i18n import language_name_local
from django.utils import translation
from django.utils.text import capfirst
from django.utils.translation import get_language
from wagtail.wagtailadmin.edit_handlers import BasePageChooserPanel, \
    BaseMultiFieldPanel, PageChooserPanel, MultiFieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index


class CustomBasePageChooserPanel(BasePageChooserPanel):
    """
    A custom base for the PageChooserPanel. Used to display a nicer label.
    """
    def render_as_field(self):
        self.bound_field.label = 'Translation page ({})'.format(
            self.field_name.replace('_link', '').upper())
        return super().render_as_field()


class CustomBasePageTranslationMultiFieldPanel(BaseMultiFieldPanel):
    """
    A custom base for the MultiFieldPanel. Returns a custom template to either
    show a hint about adding translations. If the current page is a translation,
    only a link to the original page will be shown to prevent chaining of
    translations.
    """
    template = 'wagtailadmin/custom_translation_pages_panel.html'

    def render(self):
        if self.instance.get_language() != 'en':
            # Current page already is a translation, do not let the user choose
            # additional translations
            self.template = 'wagtailadmin/custom_translation_pages_panel_' \
                            'empty.html'
        return super().render()


class TranslationFieldPanel(PageChooserPanel):
    """
    A custom PageChooserPanel, used just to inherit from the custom base model.
    """
    def bind_to_model(self, model):
        # Inherit from the custom base model.
        return type(str('_PageChooserPanel'), (CustomBasePageChooserPanel,), {
            'model': model,
            'field_name': self.field_name,
            'page_type': self.page_type,
            'can_choose_root': self.can_choose_root,
        })


class PageTranslationPanel(MultiFieldPanel):
    """
    A custom MultiFieldPanel showing a page chooser to add a translation page
    for each language.
    """
    def __init__(self):
        children = [
            TranslationFieldPanel('{}_link'.format(lang[0]))
            for lang in settings.LANGUAGES[1:]
        ]
        heading = 'Translations'
        super().__init__(children, heading, classname='')

    def bind_to_model(self, model):
        # Inherit from the custom base panel
        return type(str('_MultiFieldPanel'), (
            CustomBasePageTranslationMultiFieldPanel,), {
                        'model': model,
                        'children': [child.bind_to_model(model) for child in self.children],
                        'heading': self.heading,
                        'classname': self.classname,
                    })


class TranslatablePageMixin(models.Model):
    """This mixin adds links to translations."""

    # One link for each alternative language. Must correspond to the languages
    # set in settings.py. The default language (en) does not require a link.
    # When adding new languages: Also add id fields as search_fields below.
    fr_link = models.ForeignKey(
        Page, null=True, on_delete=models.SET_NULL, blank=True,
        related_name='+')
    es_link = models.ForeignKey(
        Page, null=True, on_delete=models.SET_NULL, blank=True,
        related_name='+')

    original_lang_code = 'en'

    content_panels = [
        PageTranslationPanel(),
    ]

    search_fields = [
        index.FilterField('url_path'),
        index.FilterField('fr_link_id'),
        index.FilterField('es_link_id'),
    ]

    @staticmethod
    def get_translated_page(page, lang_code=None):
        if lang_code is None:
            lang_code = get_language()
        if lang_code != TranslatablePageMixin.original_lang_code:
            # Try to find translation
            try:
                page = page.get_translation(lang_code) or page
            except AttributeError:
                pass
        return page

    def get_language_homepage(self):
        # Look through ancestors of this page for its language homepage
        # The language homepage is located at depth 3
        return self.get_ancestors(inclusive=True).get(depth=3)

    def get_language(self):
        """Get the language code for the current page."""
        language_homepage = self.get_language_homepage()
        # The slug of language homepages should always be set to the language
        # code
        return language_homepage.slug

    @property
    def is_original(self):
        return self.get_language() == self.original_lang_code

    def get_translation(self, lang_code):
        link_attr = self.get_link_attr(lang_code)
        translation = getattr(self, link_attr)
        if translation and translation.live is True:
            return translation

    @staticmethod
    def get_link_attr(lang_code):
        return '{}_link'.format(lang_code)

    def translation_links(self) -> list:
        """
        Get a list of tuples with [0] the language code, [1] the language name
        and [2] the url for each translation of the current page. The current
        translation is not returned.
        """
        original_page = self.original_page()
        for lang_code, _ in settings.LANGUAGES:
            lang_name = capfirst(language_name_local(lang_code))
            if lang_code == self.get_language():
                # Exclude the current language
                continue
            if lang_code == self.original_lang_code:
                yield lang_code, lang_name, original_page.url
                continue
            trans_link = original_page.get_translation(lang_code)
            if trans_link is not None:
                yield lang_code, lang_name, trans_link.url
                continue

    def original_page(self):
        """Find the original version of this page"""
        curr_lang_code = self.get_language()
        for lang_code, _ in settings.LANGUAGES:
            if curr_lang_code == lang_code:
                if lang_code == self.original_lang_code:
                    return self
                link_filter = {'{}_link'.format(curr_lang_code): self}
                original_page = type(self).objects.filter(**link_filter).first()
                if original_page:
                    return original_page.specific

    @staticmethod
    def apply_translation_filter(qs, request):
        # Apply a filter to get either original or translated pages, but not
        # both. Used for ProjectCountryPage, ProjectPage or RegionPage.
        current_language = translation.get_language_from_request(request)
        original_language = TranslatablePageMixin.original_lang_code

        if current_language == original_language:
            # If the current language is the original, limit results to only
            # these (identified by url_path)
            return qs.filter(
                url_path__startswith='/home/{}/'.format(current_language))
        else:
            # If a translation language is currently active, query all
            # original pages and the translations in the current language.
            # Then exclude all original pages with translations in the
            # current language (having a link to the translation)
            return qs.filter(
                Q(url_path__startswith='/home/{}/'.format(current_language))
                | Q(url_path__startswith='/home/{}/'.format(
                    TranslatablePageMixin.original_lang_code))).exclude(
                **{'{}_link__isnull'.format(current_language): False})

    class Meta:
        abstract = True


class LanguageRedirectionPage(Page):
    """
    This is the new root page (served at "/") and is only used to redirect to
    the respective language tree.
    """
    def serve(self, request, **kwargs):
        # Get the currently active language (or the default language)
        language = translation.get_language_from_request(request)
        return HttpResponseRedirect(self.url + language + '/')
