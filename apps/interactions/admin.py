# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment, Like

admin.site.register(Comment)
admin.site.register(Like)
