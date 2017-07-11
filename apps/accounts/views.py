# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView

from .models import UserProfile


class ProfileView(DetailView):
    template_name = 'account/profile.html'
    context_object_name = 'profile'
    model = UserProfile

    def get_object(self):
        return self.model.objects.get(
            user__username=self.kwargs['slug'])
