from django import forms
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
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

    def save(self, commit=True):
        user = super().save(commit=commit)
        if self.has_changed() and 'is_active' in self.changed_data:
            if self.cleaned_data['is_active']:
                # User has been activated
                notify_user(user)
            else:
                # User has been deactivated
                # print('>> DEACTIVATED')
                pass
        return user


class UserCreationForm(WocatUserCreationForm):
    institution = forms.ModelChoiceField(
        queryset=Institution.objects.all(),
        required=False,
        label=_('Institution'),
    )


def notify_user(user):
    domain = Site.objects.get_current()
    context = {
        'user': user,
        'project': 'WOCAT',
        'domain': domain,
        'login_url': 'http://www.{domain}{path}'.format(
            domain=domain,
            path=reverse('account_login')
        )
    }
    subject = render_to_string('users/emails/email_user_activated_subject.txt', context=context).strip()
    message = render_to_string('users/emails/email_user_activated_message.txt', context=context)
    recipient_list = [user.email]
    send_mail(subject=subject, message=message, from_email=settings.DEFAULT_FROM_EMAIL,
              recipient_list=recipient_list)
