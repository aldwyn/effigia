# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import modelform_factory
from django.views.generic import ListView
from django.views.generic import CreateView
from django.utils.text import slugify

from ..posts.models import Post
from .models import Group


class GroupListView(ListView):
    template_name = 'groups/list.html'
    context_object_name = 'groups'
    model = Group
    paginate_by = 20


class GroupItemView(ListView):
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    model = Post
    paginate_by = 20

    def get_queryset(self):
        return Group.objects.get(slug=self.kwargs['slug']).posts.all()

    def get_context_data(self, **kwargs):
        kwargs['all_posts_count'] = self.get_queryset().count()
        kwargs['group'] = Group.objects.get(slug=self.kwargs['slug'])
        kwargs['post_create_form'] = modelform_factory(Post, fields=['text'])
        return super(GroupItemView, self).get_context_data(**kwargs)


class GroupCreateView(LoginRequiredMixin, CreateView):
    template_name = 'groups/create.html'
    model = Group
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        group = form.save()
        group.slug = '{}-{}'.format(slugify(group.name), group.pk)
        group.save()
        messages.add_message(
            self.request, messages.INFO, 'You created %s.' % group)
        return super(GroupCreateView, self).form_valid(form)
