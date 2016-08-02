from django import forms
from wagtail.wagtailusers.forms import UserEditForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from wocat.institutions.models import Institution


class CustomUserEditForm(UserEditForm):
    institution = forms.ModelChoiceField(
        queryset=Institution.objects.all(),
        required=False,
        label=_('Institution'),
    )


class CustomUserCreationForm(UserCreationForm):
    institution = forms.ModelChoiceField(
        queryset=Institution.objects.all(),
        required=False,
        label=_('Institution'),
    )
