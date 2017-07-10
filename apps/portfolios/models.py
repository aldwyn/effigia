# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from core.models import EffigiaModel
from ..interactions.models import Comment, Like


class Portfolio(EffigiaModel):
    image = models.ImageField(upload_to='images/portfolios/')
    gallery = models.ForeignKey('galleries.Gallery', related_name='portfolios')
    comments = GenericRelation(Comment, related_query_name='portfolios')
    likes = GenericRelation(Like, related_query_name='portfolios')
