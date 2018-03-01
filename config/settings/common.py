# -*- coding: utf-8 -*-
"""
Django settings for WOCAT project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

import environ
from django.utils.translation import ugettext_lazy as _

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('wocat')

env = environ.Env()
env.read_env(ROOT_DIR('.env'))

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',

    'wocat.users',  # custom users app
)

CMS_APPS = (
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'taggit',
    'modelcluster',

    'wagtail.contrib.modeladmin',
    'wagtail.contrib.settings',
)

THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'django_countries',
    'django_languages',
    'easy_thumbnails',
    'compressor',
    'rest_framework',  # api
    'rest_framework.authtoken',  # token auth
    'rest_framework_swagger',  # api docs
    'django_filters',
    'maintenancemode',
    'sekizai',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    # Your stuff: custom apps go here
    'wocat.core',
    'wocat.cms',
    'wocat.styleguide',
    'wocat.institutions',
    'wocat.medialibrary',
    'wocat.news',
    'wocat.glossary',
    'wocat.search',
    'wocat.api',

    'wocat.countries',
    'wocat.languages',

    'wocat.newsletter',
    'wocat.piwik',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + CMS_APPS + THIRD_PARTY_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # maintenance mode
    'maintenancemode.middleware.MaintenanceModeMiddleware',
    # wagtail cms
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'wocat.contrib.sites.migrations',
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Eraldo Energy""", 'eraldo@eraldo.org'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db('DATABASE_URL', default='postgres:///wocat'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Berlin'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en'

# For every additional language (other than the default one), a link must be
# defined in cms/translation.py:TranslatablePageMixin. Also create a new CMS
# page in "Home" with the slug of the new language.
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    ('es', _('Spanish')),
    # See comment above when adding new languages ...
]
# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

LOCALE_PATHS = (
    str(ROOT_DIR.path('locale')),
)

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'wocat.core.context_processors.webmaster_tools_key',
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
ACCOUNT_ADAPTER = 'wocat.users.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = 'wocat.users.adapters.SocialAccountAdapter'
ACCOUNT_SIGNUP_FORM_CLASS = 'wocat.users.forms.UserForm'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/accounts/inactive/'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin'

# Your common stuff: Below this line define 3rd party library settings

# CMS
# ------------------------------------------------------------------------------
WAGTAIL_SITE_NAME = 'WOCAT'
WAGTAILADMIN_NOTIFICATION_USE_HTML = True
TAGGIT_CASE_INSENSITIVE = True
WAGTAIL_USER_EDIT_FORM = 'wocat.cms.forms.UserEditForm'
WAGTAIL_USER_CREATION_FORM = 'wocat.cms.forms.UserCreationForm'
WAGTAIL_USER_CUSTOM_FIELDS = ['institution']
ELASTICSEARCH_URL = env('ELASTICSEARCH_URL', default='')
# TODO temporary fix until upstream accepts patch: https://github.com/torchbox/wagtail/pull/2992
WAGTAILSEARCH_BACKEND = env('WAGTAILSEARCH_BACKEND', default='db')
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.{}'.format(WAGTAILSEARCH_BACKEND),
        'URLS': [ELASTICSEARCH_URL],
        'INDEX': 'wocat',
        'TIMEOUT': 30,
    }
}
# END TODO------------------------------------------------------------------

# WAGTAILDOCS_DOCUMENT_MODEL = 'core.IndexedDocument'
WAGTAIL_APPEND_SLASH = False


# EASY THUMBNAILS
# ------------------------------------------------------------------------------
THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (50, 50), 'crop': True},
        'medium': {'size': (100, 100), 'crop': True},
        'large': {'size': (200, 200), 'crop': True},
        'avatarsquare': {'size': (300, 300), 'crop': 'smart', 'upscale': True},
    },
}
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
)
THUMBNAIL_BASEDIR = 'thumbnails'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '60/m',
    },
}


# NEWSLETTER
# ------------------------------------------------------------------------------
NEWSLETTER_IS_ACTIVE_SYNC = env.bool('NEWSLETTER_IS_ACTIVE_SYNC', default=False)
NEWSLETTER_USERNAME = env('NEWSLETTER_USERNAME', default='')
NEWSLETTER_API_KEY=env('NEWSLETTER_API_KEY', default='')
NEWSLETTER_LIST_ID=env('NEWSLETTER_LIST_ID', default='')
FILTERS_DISABLE_HELP_TEXT = True

# Maintenance mode flag
MAINTENANCE_MODE = False

# Google webmaster tools
GOOGLE_WEBMASTER_TOOLS_KEY = env('GOOGLE_WEBMASTER_TOOLS_KEY', default='')

# Filename of js-file with geojson for all countries; used for the map. Relative
# to wocat/static/js
MAP_GEOJSON_FILE = env('MAP_GEOJSON_FILE', default='countries-20170619.geo.json')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',
            'formatter': 'verbose'
        },
        'mailchimp': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/mailchimp.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'WARNING',
        },
        'mailchimp_client': {
            'handlers': ['mailchimp'],
            'propagate': True,
            'level': 'INFO'
        }
    },
}
