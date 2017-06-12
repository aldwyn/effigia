# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView

from .models import Group


class GroupListView(ListView):
    template_name = 'groups/list.html'
    model = Group


class GroupItemView(DetailView):
    template_name = 'groups/item.html'
    model = Group


class GroupCreateView(CreateView):
    template_name = 'groups/create.html'
    model = Group
