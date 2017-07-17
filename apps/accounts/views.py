# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.shortcuts import redirect

from .forms import UserProfileForm
from .models import UserProfile


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'account/profile.html'
    context_object_name = 'profile'
    model = UserProfile

    def get_object(self):
        return self.model.objects.get(user__username=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['people_you_may_follow'] = get_user_model().objects.exclude(username='admin')[:5]
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'account/profile_edit.html'
    model = get_user_model()
    form_class = UserProfileForm

    def get_object(self):
        return self.model.objects.get(username=self.request.user.username)

    def get_form_kwargs(self):
        kwargs = super(ProfileUpdateView, self).get_form_kwargs()
        profile = self.object.profile
        kwargs.update({
            'initial': {
                'avatar': profile.avatar,
                'bio': profile.bio,
                'country': profile.country,
            }
        })
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.profile.avatar = form.cleaned_data['avatar']
        self.object.profile.bio = form.cleaned_data['bio']
        self.object.profile.country = form.cleaned_data['country']
        self.object.profile.save()
        return super(ProfileUpdateView, self).form_valid(form)


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'account/settings.html'
