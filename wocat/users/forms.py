from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Field, Div
from django.contrib.auth import get_user_model
from django import forms
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
        fields = ['email', 'first_name', 'last_name', 'gender', 'title', 'position', 'department', 'function',
                  'experiences', 'key_work_topics', 'address', 'address_2', 'postal_code', 'city', 'country', 'phone',
                  'phone_2', 'fax', 'fax_2', 'second_email', 'comments', 'avatar', 'institution',
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
        # Required to prevent multiple save
        pass
