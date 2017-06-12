# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from faker import Faker
from django.utils.text import slugify

from ..accounts.factories import UserFactory
from .models import Gallery


class GalleryFactory(factory.Factory):
    class Meta:
        model = Gallery

    name = factory.LazyAttribute(lambda a: ' '.join(Faker().words(nb=2)).title())
    description = factory.Faker('text')
    slug = factory.LazyAttribute(lambda a: slugify(a.name))
    created_by = UserFactory()
