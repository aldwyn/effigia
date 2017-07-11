# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from faker import Faker

from .models import Group


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.LazyAttribute(lambda a: Faker().word().title())
    description = factory.Faker('sentence')
