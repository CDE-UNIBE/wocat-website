from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    name = 'wocat.newsletter'

    def ready(self):
        from . import signals  # noqa
