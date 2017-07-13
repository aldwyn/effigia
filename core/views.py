# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.shortcuts import redirect
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


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['test_users'] = get_user_model().objects.exclude(username='admin')[:4]
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse('dashboard:home'))
        return super(IndexView, self).get(request, *args, **kwargs)


class CategoryListView(ListView):
    template_name = 'categories/list.html'
    context_object_name = 'categories'
    model = Category
    paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['all_categories_count'] = Category.objects.count()
        return super(CategoryListView, self).get_context_data(**kwargs)
