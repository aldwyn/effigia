from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.interactions.models import Following


@receiver(post_save, sender=Following)
def following_create_successful(sender, **kwargs):
    pass
