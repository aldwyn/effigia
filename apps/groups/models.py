# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.models import EffigiaModel


class Group(EffigiaModel):
    cover_image = models.ImageField(upload_to='covers/group/')
