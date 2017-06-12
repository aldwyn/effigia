# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils.text import slugify

from .models import Gallery


class GalleryListView(ListView):
    template_name = 'galleries/list.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 15


class GalleryItemView(DetailView):
    template_name = 'galleries/item.html'
    context_object_name = 'gallery'
    model = Gallery


class GalleryCreateView(CreateView):
    template_name = 'galleries/create.html'
    fields = ['name', 'description']
    model = Gallery

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        gallery = form.save()
        gallery.slug = '{}-{}'.format(slugify(gallery.name), gallery.pk)
        gallery.save()
        self.success_url = reverse('gallery:item', args=[gallery.slug])
        return super(GalleryCreateView, self).form_valid(form)


class GalleryEditView(UpdateView):
    template_name = 'galleries/item.html'
    fields = ['name', 'description']
    model = Gallery


class GalleryDeleteView(DeleteView):
    success_url = reverse_lazy('gallery:list')
    model = Gallery
