from django.db.models.signals import post_save
from django.dispatch import receiver

from wocat.users.models import User
from .client import newsletter_client


@receiver(post_save, sender=User)
def update_newsletter_subscription(sender, instance, **kwargs):
    newsletter_client.update_member(user=instance)
