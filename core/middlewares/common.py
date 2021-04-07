# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from actstream import action
from django.utils.deprecation import MiddlewareMixin

from apps.galleries.views import GalleryItemView
from apps.galleries.models import Gallery
from apps.portfolios.views import PortfolioItemView
from apps.portfolios.models import Portfolio
from apps.groups.views import GroupItemView
from apps.groups.models import Group


MODELS_FOR_SAVING_VISITS = {
    GalleryItemView: Gallery,
    GroupItemView: Group,
    PortfolioItemView: Portfolio,
}


class MiddlewareObjectMixin(object):

    def get_object(self, klass, **kwargs):
        if kwargs.get('slug'):
            return klass.objects.get(slug=kwargs['slug'])

    def is_item_view(self, view_func, view_kwargs):
        return (hasattr(view_func, 'view_class') and
                view_func.view_class in MODELS_FOR_SAVING_VISITS and
                view_kwargs.get('slug'))


class EffigiaVisitMiddleware(MiddlewareObjectMixin, MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        """ Save an action for the visited objects of the current user """
        if (self.is_item_view(view_func, view_kwargs)):
            klass = MODELS_FOR_SAVING_VISITS[view_func.view_class]
            obj = self.get_object(klass, **view_kwargs)
            if request.user.is_authenticated:
                action.send(request.user, verb='visited a %s' % obj._meta.verbose_name, target=obj)
            else:
                obj.anonymous_visits_count += 1
                obj.save()
        return view_func(request, *view_args, **view_kwargs)
