# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db.models import TimeStampedModel

from ..comments.models import Comment


class Gallery(TimeStampedModel):
    class Meta:
        ordering = ['-created']

    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    cover_image = models.ImageField(upload_to='covers/gallery/')
    category = models.ForeignKey('categories.Category', related_name='galleries')
    created_by = models.ForeignKey(get_user_model())
    likers = models.ManyToManyField(get_user_model(), related_name='galleries_liked')
    comments = GenericRelation(Comment, related_query_name='galleries')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery:item', args=[self.slug])
