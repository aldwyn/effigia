# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField
from django_extensions.db.models import TimeStampedModel


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(get_user_model(), related_name='profile')
    avatar = models.ImageField(upload_to='userprofiles/avatars')
    country = CountryField()
    bio = models.TextField()
