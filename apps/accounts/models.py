# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from django_extensions.db.models import TimeStampedModel
from django_prometheus.models import ExportModelOperationsMixin


class User(ExportModelOperationsMixin('user'), AbstractUser):

    def get_absolute_url(self):
        return reverse('account_profile', args=[self])


class UserProfile(ExportModelOperationsMixin('userprofile'), TimeStampedModel):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='userprofiles/avatars')
    is_test_user = models.BooleanField(default=False)
    country = CountryField()
    bio = models.TextField()

    def get_absolute_url(self):
        return reverse('account_profile', args=[self.user])
