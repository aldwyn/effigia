# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from .models import Comment
from ..galleries.models import Gallery
from ..portfolios.models import Portfolio


class CommentCreateView(CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        model_name = Gallery if self.kwargs['content_type'] == 'gallery' else Portfolio
        obj = model_name.objects.get(pk=self.kwargs['pk'])
        form.instance.created_by = self.request.user
        form.instance.content_object = obj
        form.save()
        messages.add_message(
            self.request, messages.INFO, 'Successfully posted a comment on %s.' % obj.name)
        self.success_url = reverse('%s:item' % self.kwargs['content_type'], args=[obj.slug])
        return super(CommentCreateView, self).form_valid(form)
