# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from imagekit import register
        import core.signals.handlers  #noqa

        from .utils import imagekit_utils

        register.generator('gallery-slideshow', imagekit_utils.GallerySlideshowImage)
        register.generator('gallery-thumbnail', imagekit_utils.GalleryCoverThumbnail)
        register.generator('portfolio-thumbnail', imagekit_utils.PortfolioThumbnail)
        register.generator('portfolio-item', imagekit_utils.PortfolioItemImage)
