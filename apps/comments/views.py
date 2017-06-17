# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from .models import Comment
from ..galleries.models import Gallery
from ..portfolios.models import Portfolio
from ..posts.models import Post


CONTENT_TYPES_MODEL = {
    'gallery': Gallery,
    'portfolio': Portfolio,
    'post': Post,
}


class CommentCreateView(CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        model_name = CONTENT_TYPES_MODEL[self.kwargs['content_type']]
        obj = model_name.objects.get(pk=self.kwargs['pk'])
        form.instance.created_by = self.request.user
        form.instance.content_object = obj
        form.save()
        messages.add_message(
            self.request, messages.INFO, 'Successfully posted a comment on %s.' % obj)
        args = [obj.pk if self.kwargs['content_type'] == 'post' else obj.slug]
        self.success_url = reverse('%s:item' % self.kwargs['content_type'], args=args)
        return super(CommentCreateView, self).form_valid(form)
