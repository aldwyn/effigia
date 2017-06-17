# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import auth_login
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.shortcuts import render


class LoginView(BaseLoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('dashboard:home')

    def form_valid(self, form):
        user = form.get_user()
        messages.add_message(
            self.request, messages.INFO, 'Welcome back, @%s!' % user.username)
        return super(LoginView, self).form_valid(form)


class LogoutView(BaseLogoutView):

    def get_next_page(self):
        messages.add_message(
            self.request, messages.INFO, 'You successfully logged out.')
        return super(LogoutView, self).get_next_page()


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('dashboard:home')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            auth_login(self.request, user)
            return redirect(reverse('dashboard:home'))
        return render(self.request, self.template_name, {'form': form})


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'
