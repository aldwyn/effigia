# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from core.models import EffigiaModel
from ..interactions.models import Comment, Like


class Gallery(EffigiaModel):
    class Meta:
        verbose_name_plural = 'galleries'

    cover_image = models.ImageField(upload_to='covers/gallery/')
    category = models.ForeignKey('core.Category', related_name='galleries')
    comments = GenericRelation(Comment, related_query_name='galleries')
    likes = GenericRelation(Like, related_query_name='galleries')
