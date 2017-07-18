# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import PermissionDenied


class ObjectOwnerMixin(object):

    def get_object(self):
        obj = super(ObjectOwnerMixin, self).get_object()
        if obj.created_by != self.request.user:
            raise PermissionDenied()


class ObjectUpdateMixin(ObjectOwnerMixin):

    def put(self, request, *args, **kwargs):
        self.__check_if_owner()
        return super(ObjectOwnerMixin, self).put(request, *args, **kwargs)


class ObjectDeleteMixin(ObjectOwnerMixin):

    def put(self, request, *args, **kwargs):
        self.__check_if_owner()
        return super(ObjectOwnerMixin, self).delete(request, *args, **kwargs)
