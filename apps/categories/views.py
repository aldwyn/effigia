# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from .models import Category


class CategoryListView(ListView):
    template_name = 'categories/list.html'
    context_object_name = 'categories'
    model = Category
    paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['all_categories_count'] = Category.objects.count()
        return super(CategoryListView, self).get_context_data(**kwargs)
