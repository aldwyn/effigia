# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from actstream.models import actor_stream
from actstream.models import user_stream
from actstream.models import Action
from actstream.models import Follow
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.views.generic import ListView

from ..galleries.models import Gallery
from .mixins import FollowingsMixin
from .mixins import RandomQuoteContextMixin
from .mixins import PeopleYouMayFollowContextMixin


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


class MyActiviesView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/my-activities.html'
    context_object_name = 'actions'
    model = Action
    paginate_by = 40

    def get_queryset(self):
        return actor_stream(self.request.user)


class BaseFeedsView(LoginRequiredMixin,
                    RandomQuoteContextMixin,
                    PeopleYouMayFollowContextMixin,
                    ListView):
    template_name = 'dashboard/feeds-base.html'
    context_object_name = 'actions'
    model = Action
    paginate_by = 30


class FeedsAllView(BaseFeedsView):

    def get_queryset(self):
        return user_stream(self.request.user)


class FeedsGalleriesView(BaseFeedsView):

    def get_queryset(self):
        return user_stream(self.request.user)


class FeedsGroupsView(BaseFeedsView):

    def get_queryset(self):
        return user_stream(self.request.user)


class BaseFollowingsView(LoginRequiredMixin,
                         PeopleYouMayFollowContextMixin,
                         ListView,
                         FollowingsMixin):
    template_name = 'dashboard/followings-base.html'
    context_object_name = 'followings'
    model = Follow
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(BaseFollowingsView, self).get_context_data(**kwargs)
        context['followed_users_count'] = self.get_followed_users().count()
        context['followed_galleries_count'] = self.get_followed_galleries().count()
        context['followed_groups_count'] = self.get_followed_groups().count()
        context['followers_count'] = self.get_followers().count()
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
