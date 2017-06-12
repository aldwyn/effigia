# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class HomeView(TemplateView):
    template_name = 'dashboard/home.html'


class NotificationsView(TemplateView):
    template_name = 'dashboard/notifications.html'


class SettingsView(TemplateView):
    template_name = 'dashboard/settings.html'
