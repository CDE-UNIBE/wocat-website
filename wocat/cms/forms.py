from django import forms
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from django_countries.widgets import CountrySelectWidget
from wagtail.wagtailusers.forms import UserEditForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _


class CustomUserEditForm(UserEditForm):
    avatar = forms.ImageField(
        required=False,
        label=_('Avatar'),
    )
    country = LazyTypedChoiceField(
        required=False,
        label=_('Country'),
        choices=countries,
    )
    organisation = forms.CharField(
        required=False,
        label=_('Organisation'),
    )
    expertise = forms.CharField(
        required=False,
        label=_('Expertise'),
    )


class CustomUserCreationForm(UserCreationForm):
    avatar = forms.ImageField(
        required=False,
        label=_('Avatar'),
    )
    country = LazyTypedChoiceField(
        required=False,
        label=_('Country'),
        choices=countries,
    )
    organisation = forms.CharField(
        required=False,
        label=_('Organisation'),
    )
    expertise = forms.CharField(
        required=False,
        label=_('Expertise'),
    )
