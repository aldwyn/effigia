# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from faker import Faker
from django.core.files.base import ContentFile
from django.utils.text import slugify

from ..accounts.factories import UserFactory
from .models import Gallery


class GalleryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Gallery

    name = factory.LazyAttribute(lambda a: ' '.join(Faker().words(nb=2)).title())
    description = factory.Faker('text')
    slug = factory.LazyAttribute(lambda a: slugify(a.name))
    cover_image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 768}
            ), 'example.jpg'
        )
    )
    created_by = UserFactory()
