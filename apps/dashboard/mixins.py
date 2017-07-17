# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from actstream.models import Follow

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
