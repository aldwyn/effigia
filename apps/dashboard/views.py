# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from actstream.models import Action
from actstream.models import actor_stream
from actstream.models import user_stream
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.views.generic import ListView

from ..galleries.models import Gallery


class HomeView(LoginRequiredMixin, RedirectView):
    permanent = True
    url = reverse_lazy('dashboard:following')


class MyGalleriesView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/my-galleries.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 15

    def get_queryset(self):
        return Gallery.objects.filter(created_by=self.request.user).order_by('-is_default')

    def get_context_data(self, **kwargs):
        context = super(MyGalleriesView, self).get_context_data(**kwargs)
        context['all_galleries_count'] = self.get_queryset().count()
        return context


class MyActiviesView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/my-activities.html'
    context_object_name = 'actions'
    model = Action
    paginate_by = 15

    def get_queryset(self):
        return actor_stream(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MyActiviesView, self).get_context_data(**kwargs)
        context['all_actions_count'] = self.get_queryset().count()
        return context


class FollowingView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/following.html'
    context_object_name = 'actions'
    model = Action
    paginate_by = 15

    def get_queryset(self):
        return user_stream(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(FollowingView, self).get_context_data(**kwargs)
        context['all_actions_count'] = self.get_queryset().count()
        context['people_you_may_follow'] = get_user_model().objects.exclude(username='admin')[:6]
        return context


class NotificationsView(TemplateView):
    template_name = 'dashboard/notifications.html'


class SettingsView(TemplateView):
    template_name = 'dashboard/settings.html'
