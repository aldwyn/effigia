# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(TimeStampedModel):
    class Meta:
        ordering = ['-created']

    text = models.TextField()
    created_by = models.ForeignKey(get_user_model(), related_name='comments')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    likers = models.ManyToManyField(get_user_model(), related_name='comments_liked')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.text[:20] + '...'
