# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from actstream import action
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from model_utils import Choices
from model_utils import FieldTracker
from model_utils.models import StatusModel
from model_utils.models import SoftDeletableModel
from model_utils.models import TimeStampedModel


class EffigiaModel(TimeStampedModel, SoftDeletableModel, StatusModel):
    class Meta:
        abstract = True

    STATUS = Choices('draft', 'published')
    name = models.CharField(max_length=255)
    is_private = models.BooleanField(default=False)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_by = models.ForeignKey(get_user_model())
    anonymous_visits_count = models.PositiveIntegerField(default=0)

    tracker = FieldTracker()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('%s:item' % self._meta.verbose_name, args=[self.slug])

    def save(self, *args, **kwargs):
        verb = 'created' if self.pk is None else 'updated'
        super(EffigiaModel, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = '{}-{}'.format(slugify(self.name), self.pk)
            super(EffigiaModel, self).save()
        action.send(self.created_by, verb='%s a %s' % (verb, self._meta.verbose_name), target=self)

    def delete(self, *args, **kwargs):
        action.send(self.created_by, verb='removed a %s' % self._meta.verbose_name, target=self)
        return super(EffigiaModel, self).delete(*args, **kwargs)


class Category(TimeStampedModel):
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
