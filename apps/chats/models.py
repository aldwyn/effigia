# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_prometheus.models import ExportModelOperationsMixin


class Chat(ExportModelOperationsMixin('chat'), TimeStampedModel):
    from_addr = models.ForeignKey(get_user_model(), related_name='message_from', on_delete=models.CASCADE)
    to_addr = models.ForeignKey(get_user_model(), related_name='message_to', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('chat:list')


class Message(ExportModelOperationsMixin('message'), TimeStampedModel):
    body = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:50] + '...'

    def get_absolute_url(self):
        return reverse('chat:list')
