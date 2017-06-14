# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import models


class Group(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_by = models.ForeignKey(get_user_model(), related_name='groups_created')
    members = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups:item', args=[self.slug])
