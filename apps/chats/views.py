# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.models import modelform_factory
from django.views.generic import ListView

from .models import Chat
from .models import Message


class ChatListView(ListView):
    template_name = 'chats/list.html'
    context_object_name = 'chats'
    model = Chat

    def get_context_data(self, **kwargs):
        kwargs['message_form'] = modelform_factory(Message, fields=('body',))()
        return super(ChatListView, self).get_context_data(**kwargs)
