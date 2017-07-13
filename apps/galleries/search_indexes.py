# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from haystack import indexes
from .models import Gallery


class GalleryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    name = indexes.NgramField()
    description = indexes.NgramField()

    def get_model(self):
        return Gallery

    def index_queryset(self, using=None):
        return self.get_model().objects.exclude(is_default=True)
