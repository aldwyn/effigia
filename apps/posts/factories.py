# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from faker import Faker
from ..accounts.factories import UserFactory
from .models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    name = factory.LazyAttribute(lambda a: ' '.join(Faker().words(nb=2)).title())
    description = factory.Faker('text')
    created_by = UserFactory()
