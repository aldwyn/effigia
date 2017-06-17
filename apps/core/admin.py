# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ..categories.models import Category
from ..chats.models import Chat, Message
from ..comments.models import Comment
from ..galleries.models import Gallery
from ..groups.models import Group
from ..portfolios.models import Portfolio
from ..posts.models import Post

admin.site.register(Category)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Gallery)
admin.site.register(Group)
admin.site.register(Portfolio)
admin.site.register(Post)
