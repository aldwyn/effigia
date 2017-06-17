# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from faker import Faker
from django.utils.text import slugify

from ..accounts.factories import UserFactory
from .models import Group


class GroupFactory(factory.Factory):
    class Meta:
        model = Group

    name = factory.LazyAttribute(lambda a: Faker().word().title())
    description = factory.Faker('sentence')
    slug = factory.LazyAttribute(lambda a: slugify(a.name))
    created_by = UserFactory()
