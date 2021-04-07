# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from ordered_model.models import OrderedModel
from ordered_model.models import OrderedModelManager

from core.models import EffigiaModel
from ..interactions.models import Comment, Like


class Portfolio(EffigiaModel, OrderedModel):
    image = models.ImageField(upload_to='images/portfolios/')
    gallery = models.ForeignKey('galleries.Gallery', related_name='portfolios', on_delete=models.CASCADE)
    comments = GenericRelation(Comment, related_query_name='portfolios')
    likes = GenericRelation(Like, related_query_name='portfolios')
    order_with_respect_to = 'gallery'

    objects = OrderedModelManager()
