# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.contrib.auth import get_user_model
from actstream.models import Follow

from core.models import Quote
from ..galleries.models import Gallery
from ..groups.models import Group


class FollowingsMixin(object):

    def get_followed_users(self):
        return Follow.objects.following_qs(self.request.user, get_user_model())

    def get_followed_galleries(self):
        return Follow.objects.following_qs(self.request.user, Gallery)

    def get_followed_groups(self):
        return Follow.objects.following_qs(self.request.user, Group)

    def get_followers(self):
        return Follow.objects.followers_qs(self.request.user)


class PeopleYouMayFollowContextMixin(object):

    def get_context_data(self, **kwargs):
        context = super(PeopleYouMayFollowContextMixin, self).get_context_data(**kwargs)
        context['people_you_may_follow'] = get_user_model().objects \
            .values('username', 'first_name', 'last_name') \
            .exclude(username='admin')[:5]
        return context


class RandomQuoteContextMixin(object):

    def get_context_data(self, **kwargs):
        context = super(RandomQuoteContextMixin, self).get_context_data(**kwargs)
        context['random_quote'] = Quote.objects.all()[random.randint(0, 1000)]
        return context
