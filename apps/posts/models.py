# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from core.models import EffigiaModel
from ..interactions.models import Comment, Like


class Post(EffigiaModel):
    group = models.ForeignKey('groups.Group', related_name='posts')
    likers = models.ManyToManyField(get_user_model(), related_name='posts_liked')
    comments = GenericRelation(Comment, related_query_name='posts')
    likes = GenericRelation(Like, related_query_name='posts')
