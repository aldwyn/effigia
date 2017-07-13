# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from haystack import indexes
from apps.galleries.models import Gallery


class GalleryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.TextField(model_attr='description')

    def get_model(self):
        return Gallery

    # def index_queryset(self, using=None):
    #     return self.get_model().objects.all()
