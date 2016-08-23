# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
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


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=30, blank=True,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=30, blank=True,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

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
        return self.name

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'email': self.email})

    @property
    def name(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{first} {last}'.format(first=self.first_name, last=self.last_name)

    def get_short_name(self):
        return self.first_name

    @property
    def email_safe(self):
        email = self.email
        return email.replace('@', '( at )')
