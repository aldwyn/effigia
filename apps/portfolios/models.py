# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Portfolio(TimeStampedModel):
    class Meta:
        ordering = ['-created']

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(get_user_model())
    gallery = models.ForeignKey('galleries.Gallery', related_name='portfolios')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True)
    likers = models.ManyToManyField(get_user_model(), related_name='portfolios_liked')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:item', args=[self.slug])
