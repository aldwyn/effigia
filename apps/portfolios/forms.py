# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.models import inlineformset_factory

from ..galleries.models import Gallery
from .models import Portfolio


PortfolioFormSet = inlineformset_factory(
    Gallery, Portfolio, fields=['name', 'image'],
    can_delete=False, extra=2, min_num=1, validate_min=True)
