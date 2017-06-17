# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.views.generic import ListView

from ..galleries.models import Gallery


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['test_users'] = get_user_model().objects.exclude(username='admin')[:4]
        return super(IndexView, self).get_context_data(**kwargs)


class HomeView(ListView):
    template_name = 'dashboard/home.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 15

    def get_queryset(self):
        return Gallery.objects.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        kwargs['all_galleries_count'] = Gallery.objects.filter(created_by=self.request.user).count()
        return super(HomeView, self).get_context_data(**kwargs)


class NotificationsView(TemplateView):
    template_name = 'dashboard/notifications.html'


class SettingsView(TemplateView):
    template_name = 'dashboard/settings.html'
