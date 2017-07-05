# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class Following(TimeStampedModel):
    class Meta:
        ordering = ['-created']

    follower = models.ForeignKey(get_user_model(), related_name='followed')
    needs_approval = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Like(TimeStampedModel):
    class Meta:
        ordering = ['-created']

    liker = models.ForeignKey(get_user_model(), related_name='liked')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Comment(TimeStampedModel):
    class Meta:
        ordering = ['-created']

    text = models.TextField()
    created_by = models.ForeignKey(get_user_model(), related_name='comments')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    likes = GenericRelation(Like, related_query_name='comments')

    def __str__(self):
        return self.text[:20] + '...'
