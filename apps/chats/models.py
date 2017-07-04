# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import models


class Chat(TimeStampedModel):
    from_addr = models.ForeignKey(get_user_model(), related_name='message_from')
    to_addr = models.ForeignKey(get_user_model(), related_name='message_to')

    def get_absolute_url(self):
        return reverse('chat:list')


class Message(TimeStampedModel):
    body = models.TextField()
    chat = models.ForeignKey(Chat)

    def __str__(self):
        return self.body[:50] + '...'

    def get_absolute_url(self):
        return reverse('chat:list')
