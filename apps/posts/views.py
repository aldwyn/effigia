# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import modelform_factory
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from ..comments.forms import CommentForm
from ..groups.models import Group
from .models import Post


class PostItemView(DetailView):
    template_name = 'posts/item.html'
    context_object_name = 'post'
    model = Post

    def get_context_data(self, **kwargs):
        kwargs['comment_form'] = CommentForm(initial={
            'content_object': self.get_object(),
            'created_by': self.request.user,
        })
        kwargs['post_edit_form'] = modelform_factory(Post, fields=('text',))(instance=self.get_object())
        return super(PostItemView, self).get_context_data(**kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['text']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.group = Group.objects.get(slug=self.kwargs['slug'])
        post = form.save()
        messages.add_message(
            self.request, messages.INFO, 'Successfully created %s.' % post)
        return super(PostCreateView, self).form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['text']

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request, messages.INFO, 'Successfully updated this post.')
        return super(PostEditView, self).form_valid(form)
