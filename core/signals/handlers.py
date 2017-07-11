# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.models import Category
from apps.accounts.models import UserProfile
from apps.galleries.models import Gallery


@receiver(post_save, sender=get_user_model())
def user_created(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        UserProfile.objects.create(user=instance)
        Gallery.objects.create(
            name='Default',
            slug=slugify('default-gallery-by-%s' % instance),
            created_by=instance,
            description=('This is the gallery intended for your default portfolio storage. '
                         'Upload portfolios here to familiarize how Effigia galleries work.'),
            category=Category.objects.get(name='Uncategorized'),
            cover_image=ContentFile(
                factory.django.ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'default-gallery-cover.jpg'
            ))
