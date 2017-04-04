from allauth.account.utils import user_pk_to_url_str
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

from wocat.users.models import User


class Command(BaseCommand):
    help = 'Send a password reset link to all users.'

    def handle(self, *args, **options):
        print('>> Sending reset links...')
        users = User.objects.all()
        for user in users:
            self.send_reset_link(user)
        print('>> ...Done processing {} users.'.format(users.count()))

    def send_reset_link(self, user):
        site = get_current_site(request=None)
        email = user.email
        token_generator = default_token_generator

        temp_key = token_generator.make_token(user)

        # send the password reset email

        path = reverse("account_reset_password_from_key",
                       kwargs=dict(uidb36=user_pk_to_url_str(user),
                                   key=temp_key))

        # Build the url.
        # url = build_absolute_uri(
        #     request, path)
        use_https = False
        url = '{protocol}://{domain}{path}'.format(
            protocol='https' if use_https else 'http',
            domain=site.domain,
            path=path
        )

        context = {
            "site": site,
            "current_site": site,
            "user": user,
            "password_reset_url": url,
            "request": None,
            "username": user.email
        }

        print('Sending to user #"{}"...'.format(user.pk))
        subject = render_to_string('users/emails/password_reset_key_subject.txt', context=context).strip()
        message = render_to_string('users/emails/password_reset_key_message.txt', context=context)
        recipient_list = [email]
        send_mail(subject=subject, message=message, from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=recipient_list)
        print('...Email sent to "{}"'.format(email))

