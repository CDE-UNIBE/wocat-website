from django import forms
from wagtail.wagtailusers.forms import UserEditForm as WocatUserEditForm
from wagtail.wagtailusers.forms import UserCreationForm as WocatUserCreationForm
from django.utils.translation import ugettext_lazy as _

from wocat.institutions.models import Institution


class UserEditForm(WocatUserEditForm):
    institution = forms.ModelChoiceField(
        queryset=Institution.objects.all(),
        required=False,
        label=_('Institution'),
    )


class UserCreationForm(WocatUserCreationForm):
    institution = forms.ModelChoiceField(
        queryset=Institution.objects.all(),
        required=False,
        label=_('Institution'),
    )
