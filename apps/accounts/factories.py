# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('username',)

    username = factory.LazyAttribute(lambda a: '{}_{}'.format(a.first_name, a.last_name).lower())
    email = factory.LazyAttribute(lambda a: '{}.{}@effigia.com'.format(a.first_name, a.last_name).lower())
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = make_password('test1234')
