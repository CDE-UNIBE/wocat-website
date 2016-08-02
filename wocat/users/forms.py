from django.conf import settings
from django.contrib.auth import get_user_model
from django import forms
from django.core.mail import send_mail


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'gender', 'title', 'position', 'department', 'function', 'experiences',
                  'key_work_topics', 'address', 'address_2', 'postal_code', 'city', 'country', 'phone', 'phone_2',
                  'fax', 'fax_2', 'second_email', 'language', 'comments', 'newsletter', 'avatar', 'institution']
        fields_required = ['first_name', 'last_name', 'gender']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields_required = getattr(self.Meta, 'fields_required', None)
        if fields_required:
            for key in self.fields:
                if key in fields_required:
                    self.fields[key].required = True

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
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
        user.language = self.cleaned_data['language']
        user.comments = self.cleaned_data['comments']
        user.newsletter = self.cleaned_data['newsletter']
        user.avatar = self.cleaned_data['avatar']
        user.institution = self.cleaned_data['institution']
        user.is_active = False
        user.save()
        self.notify_moderators(user)

    def notify_moderators(self, user):
        subject = 'subject'
        message = 'message'
        recipient_list = []
        send_mail(subject=subject, message=message, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=recipient_list)
