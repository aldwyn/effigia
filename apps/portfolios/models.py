# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django_extensions.db.models import TimeStampedModel

from ..comments.models import Comment


class Portfolio(TimeStampedModel):
    class Meta:
        ordering = ['-created']

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    created_by = models.ForeignKey(get_user_model())
    gallery = models.ForeignKey('galleries.Gallery', related_name='portfolios')
    likers = models.ManyToManyField(get_user_model(), related_name='portfolios_liked')
    comments = GenericRelation(Comment, related_query_name='portfolios')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:item', args=[self.slug])
