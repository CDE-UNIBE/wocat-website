# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from easy_thumbnails.fields import ThumbnailerImageField


@python_2_unicode_compatible
class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    avatar = ThumbnailerImageField(
        verbose_name=_('avatar'),
        upload_to='users/avatars',
        # resize_source=dict(size=(1200, 1200)),
        blank=True,
    )
    country = CountryField(
        verbose_name=_('Country'),
        blank=True,
    )
    organisation = models.CharField(
        verbose_name=_('Organisation'),
        max_length=255,
        blank=True,
    )
    expertise = models.CharField(
        verbose_name=_('Expertise'),
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
