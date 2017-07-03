# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.shortcuts import redirect
from django.utils.text import slugify

from ..galleries.models import Gallery
from ..comments.forms import CommentForm
from .models import Portfolio
from .forms import PortfolioFormSet


class PortfolioListView(ListView):
    template_name = 'portfolios/list.html'
    context_object_name = 'portfolios'

    def get_queryset(self):
        return Gallery.objects.get(slug=self.kwargs.get('slug')).portfolios.all()

    def get_context_data(self, **kwargs):
        kwargs['gallery'] = Gallery.objects.get(slug=self.kwargs.get('slug'))
        return super(PortfolioListView, self).get_context_data(**kwargs)


class PortfolioItemView(DetailView):
    template_name = 'portfolios/item.html'
    context_object_name = 'portfolio'
    model = Portfolio

    def get_context_data(self, **kwargs):
        kwargs['comment_form'] = CommentForm(initial={
            'content_object': self.get_object(),
            'created_by': self.request.user,
        })
        return super(PortfolioItemView, self).get_context_data(**kwargs)


class PortfolioCreateView(LoginRequiredMixin, CreateView):
    template_name = 'portfolios/create.html'
    model = Portfolio
    fields = ['name', 'image', 'description', 'gallery']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        portfolio = form.save()
        messages.add_message(
            self.request, messages.INFO, 'Successfully created %s.' % portfolio)
        return super(PortfolioCreateView, self).form_valid(form)


class PortfolioBulkCreateView(LoginRequiredMixin, CreateView):
    template_name = 'portfolios/bulk-create.html'

    def get_context_data(self, **kwargs):
        kwargs['gallery'] = Gallery.objects.get(slug=self.kwargs['slug'])
        return super(PortfolioBulkCreateView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        if self.request.POST and self.request.FILES:
            return PortfolioFormSet(self.request.POST, self.request.FILES)
        return PortfolioFormSet()

    def form_valid(self, form):
        gallery = Gallery.objects.get(slug=self.kwargs['slug'])
        form.instance = gallery
        instances = form.save(commit=False)
        for portfolio in instances:
            portfolio.created_by = portfolio.gallery.created_by
            portfolio.save()
            portfolio.slug = '{}-{}'.format(slugify(portfolio.name), portfolio.pk)
            portfolio.save()
        return redirect(reverse('portfolio:list', kwargs={'slug': gallery.slug}))


class PortfolioEditView(LoginRequiredMixin, UpdateView):
    template_name = 'galleries/edit.html'
    context_object_name = 'gallery'
    fields = ['name', 'image', 'description', 'category']
    model = Gallery

    def form_valid(self, form):
        gallery = form.save()
        messages.add_message(
            self.request, messages.INFO, 'Successfully updated %s.' % gallery.name)
        return super(PortfolioEditView, self).form_valid(form)


class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('gallery:list')
    model = Gallery

    def form_valid(self, form):
        gallery = Gallery.objects.get(slug=self.kwargs['slug'])
        messages.add_message(
            self.request, messages.INFO, 'Successfully deleted %s.' % gallery.name)
        return super(PortfolioDeleteView, self).form_valid(form)
