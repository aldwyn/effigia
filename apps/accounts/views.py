# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.views.generic import DetailView

from .models import UserProfile


class ProfileView(DetailView):
    template_name = 'account/profile.html'
    context_object_name = 'profile'
    model = UserProfile

    def get_object(self):
        return self.model.objects.get(
            user__username=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['people_you_may_follow'] = get_user_model().objects.exclude(username='admin')[:5]
        return context
