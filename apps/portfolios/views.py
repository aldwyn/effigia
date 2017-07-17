# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.shortcuts import redirect

from ..galleries.models import Gallery
from ..interactions.forms import CommentForm
from ..interactions.models import Like
from .models import Portfolio
from .forms import PortfolioFormSet


class PortfolioListView(ListView):
    template_name = 'portfolios/list.html'
    context_object_name = 'portfolios'
    model = Portfolio
    paginate_by = 20

    def get_queryset(self):
        return Gallery.objects.get(slug=self.kwargs.get('slug')).portfolios.all()

    def get_context_data(self, **kwargs):
        context = super(PortfolioListView, self).get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.get(slug=self.kwargs.get('slug'))
        return context


class PortfolioItemView(DetailView):
    template_name = 'portfolios/item.html'
    context_object_name = 'portfolio'
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(PortfolioItemView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm(initial={
            'content_object': self.get_object(),
            'created_by': self.request.user,
        })
        content_type = ContentType.objects.get_for_model(Portfolio)
        if self.request.user.is_authenticated():
            context['liked'] = Like.objects.filter(
                liker=self.request.user,
                content_type=content_type,
                object_id=context['object'].pk).first()
        return context


class PortfolioCreateView(LoginRequiredMixin, CreateView):
    template_name = 'portfolios/create.html'
    model = Portfolio
    fields = ['name', 'image', 'description', 'gallery']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        portfolio = form.save()
        messages.add_message(
            self.request, messages.INFO, 'You created %s.' % portfolio)
        return super(PortfolioCreateView, self).form_valid(form)


class PortfolioBulkCreateView(LoginRequiredMixin, CreateView):
    template_name = 'portfolios/bulk-create.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioBulkCreateView, self).get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.get(slug=self.kwargs['slug'])
        return context

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
        return redirect(reverse('portfolio:list', kwargs={'slug': gallery.slug}))


class PortfolioEditView(LoginRequiredMixin, UpdateView):
    template_name = 'portfolios/edit.html'
    context_object_name = 'portfolio'
    fields = ['name', 'image', 'description']
    model = Portfolio

    def form_valid(self, form):
        gallery = form.save()
        messages.add_message(
            self.request, messages.INFO, 'You updated %s.' % gallery.name)
        return super(PortfolioEditView, self).form_valid(form)


class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('gallery:list')
    model = Gallery

    def form_valid(self, form):
        gallery = Gallery.objects.get(slug=self.kwargs['slug'])
        messages.add_message(
            self.request, messages.INFO, 'You deleted %s.' % gallery.name)
        return super(PortfolioDeleteView, self).form_valid(form)
