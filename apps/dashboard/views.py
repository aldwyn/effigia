# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from actstream.models import Action
from actstream.models import user_stream
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.views.generic import ListView
from django.shortcuts import redirect

from ..galleries.models import Gallery


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['test_users'] = get_user_model().objects.exclude(username='admin')[:4]
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse('dashboard:home'))
        return super(IndexView, self).get(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, RedirectView):
    permanent = True
    url = reverse_lazy('dashboard:my-galleries')


class MyGalleriesView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/my-galleries.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 15

    def get_queryset(self):
        return Gallery.objects.filter(created_by=self.request.user)

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
        return self.request.user.actor_actions.all()

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
        return user_stream(self.request.user, with_user_activity=True)

    def get_context_data(self, **kwargs):
        context = super(FollowingView, self).get_context_data(**kwargs)
        context['all_actions_count'] = self.get_queryset().count()
        return context


class NotificationsView(TemplateView):
    template_name = 'dashboard/notifications.html'


class SettingsView(TemplateView):
    template_name = 'dashboard/settings.html'
