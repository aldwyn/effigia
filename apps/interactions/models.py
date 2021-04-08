# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from actstream import action
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.models import TimeStampedModel
from django_prometheus.models import ExportModelOperationsMixin


class Like(ExportModelOperationsMixin('like'), TimeStampedModel):
    liker = models.ForeignKey(get_user_model(), related_name='liked', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)
        action.send(self.liker,
                    verb='liked a %s' % self.content_object._meta.verbose_name,
                    target=self.content_object)

    def delete(self, *args, **kwargs):
        action.send(self.liker,
                    verb='unliked a %s' % self.content_object._meta.verbose_name,
                    target=self.content_object)
        return super(Like, self).delete(*args, **kwargs)


class Comment(ExportModelOperationsMixin('comment'), TimeStampedModel):
    text = models.TextField()
    created_by = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE)
    likes = GenericRelation(Like, related_query_name='comments')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '@%s\'s comment' % self.created_by

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        action.send(self.created_by,
                    verb='commented on a %s' % self.content_object._meta.verbose_name,
                    target=self.content_object)

    def delete(self, *args, **kwargs):
        action.send(self.created_by,
                    verb='removed a comment from a %s' % self.content_object._meta.verbose_name,
                    target=self.content_object)
        return super(Comment, self).delete(*args, **kwargs)
