# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from haystack.generic_views import SearchView

from core.models import Category
from ..interactions.forms import CommentForm
from ..interactions.models import Like
from .models import Gallery


class GalleryListQuerySetMixin(object):

    def get_queryset(self):
        return super(GalleryListQuerySetMixin, self).get_queryset() \
            .annotate(num_portfolios=Count('portfolios')) \
            .filter(num_portfolios__gt=0)


class BaseGalleryListView(GalleryListQuerySetMixin, ListView):
    template_name = 'galleries/list.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 15
    include_defaults = False

    def get_context_data(self, **kwargs):
        context = super(BaseGalleryListView, self).get_context_data(**kwargs)
        context['page_header'] = 'All Galleries'
        return context


class GalleryListView(SearchView):
    template_name = 'galleries/list.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(GalleryListView, self).get_context_data(**kwargs)
        context['page_header'] = 'All Galleries'
        if self.request.GET.get('q'):
            context['page_header'] = 'Results for "%s"' % self.request.GET.get('q')
        return context


class GalleryByCategoryListView(BaseGalleryListView):

    def get_queryset(self):
        return super(GalleryByCategoryListView, self).get_queryset() \
            .filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(GalleryByCategoryListView, self).get_context_data(**kwargs)
        context['page_header'] = Category.objects.get(slug=self.kwargs['slug']).name
        return context


class GalleryItemView(DetailView):
    template_name = 'galleries/item.html'
    context_object_name = 'gallery'
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(GalleryItemView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['featured_portfolios'] = context['object'].portfolios.all()[:3]
        content_type = ContentType.objects.get_for_model(Gallery)
        if self.request.user.is_authenticated():
            context['liked'] = Like.objects.filter(
                liker=self.request.user,
                content_type=content_type,
                object_id=context['object'].pk).first()
        return context


class GalleryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'galleries/create.html'
    fields = ['name', 'description', 'category', 'cover_image']
    model = Gallery

    def get_form(self, form_class=None):
        if self.request.POST and self.request.FILES:
            return self.get_form_class()(self.request.POST, self.request.FILES)
        return self.get_form_class()()

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        gallery = form.save()
        messages.add_message(
            self.request, messages.INFO, 'You created %s.' % gallery.name)
        return super(GalleryCreateView, self).form_valid(form)


class GalleryEditView(LoginRequiredMixin, UpdateView):
    template_name = 'galleries/edit.html'
    context_object_name = 'gallery'
    fields = ['name', 'description', 'category', 'cover_image']
    model = Gallery

    def form_valid(self, form):
        gallery = form.save()
        messages.add_message(
            self.request, messages.INFO, 'You updated %s.' % gallery.name)
        return super(GalleryEditView, self).form_valid(form)


class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('gallery:list')
    model = Gallery

    def form_valid(self, form):
        gallery = Gallery.objects.get(slug=self.kwargs['slug'])
        messages.add_message(
            self.request, messages.INFO, 'You deleted %s.' % gallery.name)
        return super(GalleryDeleteView, self).form_valid(form)
