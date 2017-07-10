# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        import core.signals.handlers  #noqa
        from actstream import registry
        from django.contrib.auth import get_user_model
        from imagekit import register
        from .utils import imagekit_utils

        registry.register(get_user_model())

        register.generator('gallery-slideshow', imagekit_utils.GallerySlideshowImage)
        register.generator('gallery-thumbnail', imagekit_utils.GalleryCoverThumbnail)
        register.generator('gallery-jumbotron', imagekit_utils.GalleryCoverJumbotron)
        register.generator('portfolio-thumbnail', imagekit_utils.PortfolioThumbnail)
        register.generator('portfolio-item', imagekit_utils.PortfolioItemImage)
        register.generator('feed-card-thumbnail', imagekit_utils.FeedCardThumbnail)
