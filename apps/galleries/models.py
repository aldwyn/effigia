# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Gallery(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_by = models.ForeignKey(get_user_model())
