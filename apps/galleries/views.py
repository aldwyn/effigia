# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils.text import slugify

from ..categories.models import Category
from .models import Gallery


class GalleryListView(ListView):
    template_name = 'galleries/list.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 15

    def get_context_data(self, **kwargs):
        kwargs['all_galleries_count'] = self.get_queryset().count()
        kwargs['page_header'] = 'All Galleries'
        return super(GalleryListView, self).get_context_data(**kwargs)


class GalleryByCategoryListView(ListView):
    template_name = 'galleries/list.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 15

    def get_queryset(self):
        return Gallery.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        category = Category.objects.get(slug=self.kwargs['slug'])
        kwargs['all_galleries_count'] = self.get_queryset().count()
        kwargs['page_header'] = category.name
        return super(GalleryByCategoryListView, self).get_context_data(**kwargs)


class GalleryByUserListView(ListView):
    template_name = 'galleries/list.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 15

    def get_queryset(self):
        return Gallery.objects.filter(created_by__username=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        user = get_user_model().objects.get(username=self.kwargs['slug'])
        kwargs['all_galleries_count'] = self.get_queryset().count()
        kwargs['page_header'] = "%s's Galleries" % user.get_full_name()
        return super(GalleryByUserListView, self).get_context_data(**kwargs)


class GalleryItemView(DetailView):
    template_name = 'galleries/item.html'
    context_object_name = 'gallery'
    model = Gallery


class GalleryCreateView(CreateView):
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
        gallery.slug = '{}-{}'.format(slugify(gallery.name), gallery.pk)
        gallery.save()
        messages.add_message(
            self.request, messages.INFO, 'Successfully created %s.' % gallery.name)
        return super(GalleryCreateView, self).form_valid(form)


class GalleryEditView(UpdateView):
    template_name = 'galleries/edit.html'
    context_object_name = 'gallery'
    fields = ['name', 'description', 'category', 'cover_image']
    model = Gallery

    def form_valid(self, form):
        gallery = form.save()
        messages.add_message(
            self.request, messages.INFO, 'Successfully updated %s.' % gallery.name)
        return super(GalleryEditView, self).form_valid(form)


class GalleryDeleteView(DeleteView):
    success_url = reverse_lazy('gallery:list')
    model = Gallery

    def form_valid(self, form):
        gallery = Gallery.objects.get(slug=self.kwargs['slug'])
        messages.add_message(
            self.request, messages.INFO, 'Successfully deleted %s.' % gallery.name)
        return super(GalleryDeleteView, self).form_valid(form)
