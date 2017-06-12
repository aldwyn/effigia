# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Portfolio(TimeStampedModel):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(get_user_model())
    gallery = models.ForeignKey('galleries.Gallery', related_name='portfolios')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True)
    categories = models.ManyToManyField('categories.Category', related_name='portfolios')
    likers = models.ManyToManyField(get_user_model(), related_name='portfolios_liked')
