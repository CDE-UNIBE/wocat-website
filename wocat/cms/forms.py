from django import forms
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from django_countries.widgets import CountrySelectWidget
from wagtail.wagtailusers.forms import UserEditForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from wocat.institutions.models import Institution


class CustomUserEditForm(UserEditForm):
    institution = forms.ModelChoiceField(
        queryset=Institution.objects.all(),
        required=False,
        label=_('Institution'),
    )
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
    institution = forms.ModelChoiceField(
        queryset=Institution.objects.all(),
        required=False,
        label=_('Institution'),
    )
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
