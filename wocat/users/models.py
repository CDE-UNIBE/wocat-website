# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from easy_thumbnails.fields import ThumbnailerImageField
from wagtail.wagtailsnippets.models import register_snippet

from wocat.institutions.models import Institution


@register_snippet
class UserExperience(models.Model):
    name = models.CharField(
        _('Experience'),
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


@register_snippet
class UserKeyWorkTopic(models.Model):
    name = models.CharField(
        _('Key work topics'),
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class User(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = (
        (MALE, _('Mr')),
        (FEMALE, _('Mrs')),
    )
    gender = models.CharField(
        verbose_name=_('Salutation'),
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        blank=True,
    )
    position = models.CharField(
        verbose_name=_('Position'),
        max_length=255,
        blank=True,
    )
    department = models.CharField(
        verbose_name=_('Department'),
        max_length=255,
        blank=True,
    )
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    FUNCTION_CHOICES = (
        (LEVEL_1, _('SLM specialists field level')),
        (LEVEL_2, _('SLM specialists (sub-)national level')),
        (LEVEL_3, _('SLM specialists regional and global levels')),
    )
    function = models.PositiveSmallIntegerField(
        verbose_name=_('Your function'),
        choices=FUNCTION_CHOICES,
        blank=True, null=True,
    )
    experiences = models.ManyToManyField(
        UserExperience,
        blank=True,
    )
    key_work_topics = models.ManyToManyField(
        UserKeyWorkTopic,
        blank=True,
    )

    address = models.CharField(
        _('Address Information'),
        max_length=255,
        blank=True,
    )
    address_2 = models.CharField(
        _('Address 2'),
        max_length=255,
        blank=True,
    )
    postal_code = models.CharField(
        _('Postal code'),
        max_length=255,
        blank=True,
    )
    city = models.CharField(
        _('City'),
        max_length=255,
        blank=True,
    )
    country = CountryField(
        verbose_name=_('Country'),
        blank=True,
    )
    phone = models.CharField(
        _('Phone'),
        max_length=255,
        blank=True,
    )
    phone_2 = models.CharField(
        _('Phone 2'),
        max_length=255,
        blank=True,
    )
    fax = models.CharField(
        _('Fax'),
        max_length=255,
        blank=True,
    )
    fax_2 = models.CharField(
        _('Fax 2'),
        max_length=255,
        blank=True,
    )
    second_email = models.EmailField(
        _('Second email'),
        blank=True,
    )
    ENGLISH = 'en'
    GERMAN = 'de'
    LANGUAGE_CHOICES = (
        (ENGLISH, _('English')),
        (GERMAN, _('Deutsch')),
    )
    language = models.CharField(
        verbose_name=_('Language'),
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
    )
    comments = models.TextField(
        verbose_name=_('Comments'),
        blank=True,
    )
    newsletter = models.BooleanField(
        _('Newsletter subscription'),
        default=True,
    )
    avatar = ThumbnailerImageField(
        verbose_name=_('avatar'),
        upload_to='users/avatars',
        # resize_source=dict(size=(1200, 1200)),
        blank=True,
    )
    institution = models.ForeignKey(
        Institution,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
