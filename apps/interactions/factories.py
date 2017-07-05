# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory

from ..accounts.factories import UserFactory
from .models import Comment


class CommentFactory(factory.Factory):
    class Meta:
        model = Comment

    text = factory.Faker('text')
    created_by = UserFactory()
