# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
import random
from faker import Faker
from django.utils.text import slugify

from ..accounts.factories import UserFactory
from .models import Portfolio


class PortfolioFactory(factory.Factory):
    class Meta:
        model = Portfolio

    name = factory.LazyAttribute(
        lambda a: ' '.join(Faker().words(nb=random.randint(2, 5))).title())
    description = factory.Faker('text')
    image = ''
    slug = factory.LazyAttribute(lambda a: slugify(a.name))
    created_by = UserFactory()
