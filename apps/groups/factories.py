# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from django.core.files.base import ContentFile
from faker import Faker

from .models import Group


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.LazyAttribute(lambda a: Faker().word().title())
    description = factory.Faker('sentence')
    cover_image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 768}
            ), 'group-cover.jpg'
        )
    )
