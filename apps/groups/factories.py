# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from django.utils.text import slugify

from ..accounts.factories import UserFactory
from .models import Group


class GroupFactory(factory.Factory):
    class Meta:
        model = Group

    name = factory.Faker('word')
    description = factory.Faker('text')
    slug = factory.LazyAttribute(lambda a: slugify(a.name))
    created_by = UserFactory()
