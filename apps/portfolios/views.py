# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView

from ..galleries.models import Gallery
from .models import Portfolio


class PortfolioListView(ListView):
    template_name = 'portfolios/list.html'
    context_object_name = 'portfolios'

    def get_queryset(self):
        return Gallery.objects.get(slug=self.kwargs.get('slug')).portfolios.all()


class PortfolioItemView(DetailView):
    template_name = 'portfolios/item.html'
    context_object_name = 'portfolio'
    model = Portfolio


class PortfolioCreateView(CreateView):
    template_name = 'portfolios/create.html'
    model = Portfolio
