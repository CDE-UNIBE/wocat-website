from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Submit, Row, Field, Div
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.template.defaultfilters import linebreaksbr
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from wocat.cms.models import TermsSettings
from wocat.countries.models import Country


class FullUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        exclude = []


class UserForm(forms.ModelForm):
    unccd = forms.BooleanField(
        label=_('I’m responsible for the reporting of UNCCD Best Practices in SLM'),
        required=False,
    )
    unccd_country = forms.ChoiceField(
        choices=[],
        required=False,
    )
    key_work_topics_2 = forms.CharField(
        max_length=255,
        required=False,
        label=_("Other key work topics")
    )
    terms_and_conditions = forms.BooleanField(
        label=_('I accept the terms and conditions.'),
        required=True,
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'gender', 'title', 'position', 'department', 'function', 'experiences',
                  'key_work_topics', 'address', 'address_2', 'postal_code', 'city', 'country', 'phone', 'phone_2',
                  'fax', 'fax_2', 'second_email', 'comments', 'avatar', 'institution', 'email',
                  'newsletter', 'terms_and_conditions']
        fields_required = ['first_name', 'last_name', 'gender']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unccd_country'].choices = ((country.code, country) for country in Country.objects.all())
        self.fields['unccd_country'].widget.choices = self.fields['unccd_country'].choices

        # Update the required fields.
        fields_required = getattr(self.Meta, 'fields_required', None)
        if fields_required:
            for key in self.fields:
                if key in fields_required:
                    self.fields[key].required = True
                if key == 'institution':
                    email_link = '(email link)'
                    self.fields[
                        key].help_text = '*If your Institution is missing, please contact the WOCAT Secretariat {link}'.format(
                        link=email_link)

        # Update terms label link.
        settings = TermsSettings.objects.first()
        if settings:
            url = settings.target.url if settings.target else ''
            text = settings.name
            text_link = _('I accept the <a href="{url}" target="_blank">{text}</a>.').format(url=url, text=text)
            self.fields['terms_and_conditions'].label = text_link

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Row(
                    Field('gender', wrapper_class="col-sm-6"),
                    Field('title', wrapper_class="col-sm-6"),
                    Field('first_name', wrapper_class="col-sm-6"),
                    Field('last_name', wrapper_class="col-sm-6"),
                    # 'language',
                    Field('country', wrapper_class="col-sm-6"),
                    Field('email', wrapper_class="col-sm-6"),
                    Field('password1', wrapper_class="col-sm-6"),
                    Field('password2', wrapper_class="col-sm-6"),
                    Field('institution', wrapper_class="col-sm-6"),
                ),
            ),
            Fieldset(
                _('Address information'),
                Row(
                    Field('address', wrapper_class="col-sm-6"),
                    Field('address_2', wrapper_class="col-sm-6"),
                    Field('phone', wrapper_class="col-sm-6"),
                    Field('phone_2', wrapper_class="col-sm-6"),
                    Field('fax', wrapper_class="col-sm-6"),
                    Field('fax_2', wrapper_class="col-sm-6"),
                    Field('postal_code', wrapper_class="col-sm-6"),
                    Field('city', wrapper_class="col-sm-6"),
                    Field('comments', wrapper_class="col-sm-6"),
                    Field('second_email', wrapper_class="col-sm-6"),
                    Field('avatar', wrapper_class="col-sm-6"),
                    Div(
                        Field('unccd'),
                        Field('unccd_country'),
                        css_class="col-sm-6"
                    ),
                ),
            ),
            Fieldset(
                _('Key work topics'),
                Row(
                    Field('key_work_topics', wrapper_class="col-sm-6"),
                    Field('key_work_topics_2', wrapper_class="col-sm-6"),
                ),
            ),
            Fieldset(
                _('Function and WOCAT experiences'),
                Row(
                    Field('function', wrapper_class="col-sm-6"),
                    Field('position', wrapper_class="col-sm-6"),
                    Field('department', wrapper_class="col-sm-6"),
                    Field('experiences', wrapper_class="col-sm-6"),
                ),
            ),
            'newsletter',
            'terms_and_conditions',
        )
        self.helper.add_input(Submit('submit', _('Send')))


def signup(self, request, user):
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    user.gender = self.cleaned_data['gender']
    user.title = self.cleaned_data['title']
    user.position = self.cleaned_data['position']
    user.department = self.cleaned_data['department']
    user.function = self.cleaned_data['function']
    user.experiences = self.cleaned_data['experiences']
    user.key_work_topics = self.cleaned_data['key_work_topics']
    user.address = self.cleaned_data['address']
    user.address_2 = self.cleaned_data['address_2']
    user.postal_code = self.cleaned_data['postal_code']
    user.city = self.cleaned_data['city']
    user.country = self.cleaned_data['country']
    user.phone = self.cleaned_data['phone']
    user.phone_2 = self.cleaned_data['phone_2']
    user.fax = self.cleaned_data['fax']
    user.fax_2 = self.cleaned_data['fax_2']
    user.second_email = self.cleaned_data['second_email']
    # user.language = self.cleaned_data['language']
    user.comments = self.cleaned_data['comments']
    user.avatar = self.cleaned_data['avatar']
    user.institution = self.cleaned_data['institution']
    user.newsletter = self.cleaned_data['newsletter']
    user.terms_and_conditions = self.cleaned_data['terms_and_conditions']
    # user.is_active = False
    user.save()
    self.send_instruction_message(request, user)
    self.notify_moderators(user)


def send_instruction_message(self, request, user):
    context = {
        'salutation': user.salutation,
        'name': user.name,
        'email': user.email,
    }
    message = render_to_string('users/post_signup_message.html', context=context)
    message = linebreaksbr(message)
    messages.info(request, message)


def notify_moderators(self, user):
    context = {
        'user': user,
        'project': 'WOCAT',
        'management_url': 'http://www.{domain}/cms/users/{id}/'.format(
            domain=Site.objects.get_current(),
            id=user.id
        )
    }
    subject = render_to_string('users/emails/email_signup_moderation_request_subject.txt', context=context).strip()
    message = render_to_string('users/emails/email_signup_moderation_request_message.txt', context=context)
    recipient_list = []
    group, created = Group.objects.get_or_create(name='Signup Moderators')
    if group:
        recipient_list += list(group.user_set.values_list('email', flat=True))
    send_mail(subject=subject, message=message, from_email=settings.DEFAULT_FROM_EMAIL,
              recipient_list=recipient_list)
