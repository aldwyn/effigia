from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from imagekit.processors import ResizeToFit


class GallerySlideshowImage(ImageSpec):
    processors = [ResizeToFill(750, 500)]
    format = 'JPEG'
    options = {'quality': 30}


class GalleryCoverThumbnail(ImageSpec):
    processors = [ResizeToFill(340, 250)]
    format = 'JPEG'
    options = {'quality': 60}


class PortfolioThumbnail(ImageSpec):
    processors = [ResizeToFill(340, 250)]
    format = 'JPEG'
    options = {'quality': 60}


class PortfolioItemImage(ImageSpec):
    processors = [ResizeToFit(700, 500)]
    format = 'JPEG'
    options = {'quality': 60}
