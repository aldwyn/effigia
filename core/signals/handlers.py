from actstream import action
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.galleries.models import Gallery


@receiver(post_save, sender=Gallery)
def gallery_created(sender, instance, created, **kwargs):
    pass
