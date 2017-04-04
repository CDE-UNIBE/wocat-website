from wagtail_modeltranslation.translation import *
from wagtail_modeltranslation.translator import TranslationOptions as WagtailTranslationOptions
from wagtail_modeltranslation.decorators import register

from .models import *


@register(ContentPage)
class ContentPageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'content',
    )


@register(HomePage)
class HomePageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'about_link_text',
        'content',
    )


@register(ProjectsAndCountiesPage)
class ProjectsAndCountiesPageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'content',
    )


#@register(ProjectsPage)
#class ProjectsPageTR(WagtailTranslationOptions):
#    fields = (
#        'content',
#    )


@register(ProjectPage)
class ProjectPageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'content',
    )


@register(ProjectCountriesPage)
class ProjectCountriesPageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'content',
    )


@register(ProjectCountryPage)
class ProjectCountryPageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'content',
    )


#@register(CountriesPage)
#class CountriesPageTR(WagtailTranslationOptions):
#    fields = (
#        'content',
#    )


@register(CountryPage)
class CountryPageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'content',
    )


#@register(RegionsPage)
#class RegionsPageTR(WagtailTranslationOptions):
#    fields = (
#        'content',
#    )


@register(RegionPage)
class RegionPageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'content',
    )


@register(MembersPage)
class MembersPageTR(WagtailTranslationOptions):
    fields = (
        'content',
    )


@register(InstitutionsPage)
class InstitutionsPageTR(WagtailTranslationOptions):
    fields = (
        'content',
    )


@register(NewsAndEventsPage)
class NewsAndEventsPageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'content',
    )


@register(EventsPage)
class EventsPageTR(WagtailTranslationOptions):
    fields = (
        'lead',
        'content',
    )
