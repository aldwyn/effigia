# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory

from ..accounts.factories import UserFactory
from .models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    text = factory.Faker('text')
    created_by = UserFactory()
