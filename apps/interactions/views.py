# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import RedirectView

from .models import Comment
from .models import Following
from .models import Like
from ..galleries.models import Gallery
from ..groups.models import Group
from ..portfolios.models import Portfolio
from ..posts.models import Post


CONTENT_TYPES_MODEL = {
    'comment': Comment,
    'gallery': Gallery,
    'group': Group,
    'portfolio': Portfolio,
    'post': Post,
    'user': get_user_model(),
}


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        model_name = CONTENT_TYPES_MODEL[self.kwargs['content_type']]
        obj = model_name.objects.get(pk=self.kwargs['pk'])
        form.instance.created_by = self.request.user
        form.instance.content_object = obj
        form.save()
        messages.add_message(
            self.request, messages.INFO, 'You posted a comment on %s.' % obj)
        self.success_url = obj.get_absolute_url()
        return super(CommentCreateView, self).form_valid(form)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment


class FollowingCreateView(LoginRequiredMixin, CreateView):
    model = Following
    fields = []

    def form_valid(self, form):
        model_name = CONTENT_TYPES_MODEL[self.kwargs['content_type']]
        obj = model_name.objects.get(pk=self.kwargs['pk'])
        form.instance.follower = self.request.user
        form.instance.content_object = obj
        form.save()
        messages.add_message(self.request, messages.INFO, 'You followed %s.' % obj)
        self.success_url = obj.get_absolute_url()
        return super(FollowingCreateView, self).form_valid(form)


class FollowingDeleteView(LoginRequiredMixin, DeleteView):
    model = Following

    def delete(self, request, *args, **kwargs):
        following = Following.objects.get(pk=self.kwargs['pk'])
        obj = following.content_object
        self.success_url = obj.get_absolute_url()
        following.delete()
        messages.add_message(self.request, messages.INFO, 'You unfollowed %s.' % obj)
        return redirect(obj.get_absolute_url())


class LikeCreateView(LoginRequiredMixin, CreateView):
    model = Like
    fields = []

    def form_valid(self, form):
        model_name = CONTENT_TYPES_MODEL[self.kwargs['content_type']]
        obj = model_name.objects.get(pk=self.kwargs['pk'])
        form.instance.liker = self.request.user
        form.instance.content_object = obj
        form.save()
        messages.add_message(
            self.request, messages.INFO, 'You liked %s.' % obj)
        self.success_url = obj.get_absolute_url()
        return super(LikeCreateView, self).form_valid(form)


class LikeDeleteView(LoginRequiredMixin, DeleteView):
    model = Like

    def delete(self, request, *args, **kwargs):
        like = Like.objects.get(pk=self.kwargs['pk'])
        obj = like.content_object
        self.success_url = obj.get_absolute_url()
        like.delete()
        messages.add_message(self.request, messages.INFO, 'You unliked %s.' % obj)
        return redirect(obj.get_absolute_url())


class JoinGroupCreateView(LoginRequiredMixin, RedirectView):

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(slug=self.kwargs['slug'])
        return redirect(group.get_absolute_url())


class LeaveGroupCreateView(LoginRequiredMixin, RedirectView):

    def get(self, request, *args, **kwargs):
        pass
