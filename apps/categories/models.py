# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
