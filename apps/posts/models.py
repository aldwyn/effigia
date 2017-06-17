# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models

from ..comments.models import Comment


class Post(TimeStampedModel):
    class Meta:
        ordering = ['-created']

    text = models.TextField()
    group = models.ForeignKey('groups.Group', related_name='posts')
    created_by = models.ForeignKey(get_user_model(), related_name='posts_created')
    likers = models.ManyToManyField(get_user_model(), related_name='posts_liked')
    comments = GenericRelation(Comment, related_query_name='posts')

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse('post:item', args=[self.pk])
