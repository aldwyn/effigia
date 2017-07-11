# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Category


def handler400(request):
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response


def handler403(request):
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


class CategoryListView(ListView):
    template_name = 'categories/list.html'
    context_object_name = 'categories'
    model = Category
    paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['all_categories_count'] = Category.objects.count()
        return super(CategoryListView, self).get_context_data(**kwargs)
