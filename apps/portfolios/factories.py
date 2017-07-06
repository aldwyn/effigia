# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
import random
from faker import Faker
from django.core.files.base import ContentFile
from django.utils.text import slugify

from ..accounts.factories import UserFactory
from .models import Portfolio


class PortfolioFactory(factory.Factory):
    class Meta:
        model = Portfolio

    name = factory.LazyAttribute(
        lambda a: ' '.join(Faker().words(nb=random.randint(2, 5))).title())
    description = factory.Faker('text')
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 768}
            ), 'example.jpg'
        )
    )
    slug = factory.LazyAttribute(lambda a: slugify(a.name))
    created_by = UserFactory()
