# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from actstream.models import actor_stream
from actstream.models import user_stream
from actstream.models import Action
from actstream.models import Follow
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.views.generic import ListView

from core.models import Quote
from ..galleries.models import Gallery
from ..groups.models import Group
from .mixins import FollowingsMixin


class HomeView(LoginRequiredMixin, RedirectView):
    permanent = True
    url = reverse_lazy('dashboard:feeds-all')


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
    paginate_by = 40

    def get_queryset(self):
        return actor_stream(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MyActiviesView, self).get_context_data(**kwargs)
        context['all_actions_count'] = len(self.get_queryset())
        return context


class BaseFeedsView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/feeds-base.html'
    context_object_name = 'actions'
    model = Action
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(BaseFeedsView, self).get_context_data(**kwargs)
        context['all_actions_count'] = len(self.get_queryset())
        context['random_quote'] = Quote.objects.all()[random.randint(0, 1000)]
        context['people_you_may_follow'] = get_user_model().objects.exclude(username='admin')[:5]
        return context


class FeedsAllView(BaseFeedsView):

    def get_queryset(self):
        return user_stream(self.request.user)


class FeedsGalleriesView(BaseFeedsView):

    def get_queryset(self):
        return user_stream(self.request.user)


class FeedsGroupsView(BaseFeedsView):

    def get_queryset(self):
        return user_stream(self.request.user)


class BaseFollowingsView(LoginRequiredMixin, FollowingsMixin, ListView):
    template_name = 'dashboard/followings-base.html'
    context_object_name = 'followings'
    model = Follow
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BaseFollowingsView, self).get_context_data(**kwargs)
        context['all_followings_count'] = len(self.get_queryset())
        context['followed_users_count'] = len(self.get_followed_users())
        context['followed_galleries_count'] = len(self.get_followed_galleries())
        context['followed_groups_count'] = len(self.get_followed_groups())
        context['followers_count'] = len(self.get_followers())
        context['random_quote'] = Quote.objects.all()[random.randint(0, 1000)]
        context['people_you_may_follow'] = get_user_model().objects.exclude(username='admin')[:5]
        return context


class FollowingsUsersView(BaseFollowingsView):

    def get_queryset(self):
        return self.get_followed_users()


class FollowingsGalleriesView(BaseFollowingsView):

    def get_queryset(self):
        return self.get_followed_galleries()


class FollowingsGroupsView(BaseFollowingsView):

    def get_queryset(self):
        return self.get_followed_groups()


class FollowingsFollowersView(BaseFollowingsView):

    def get_queryset(self):
        return self.get_followers()


class NotificationsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/notifications.html'


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/settings.html'
