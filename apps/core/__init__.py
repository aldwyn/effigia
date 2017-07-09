from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill, ResizeToFit


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


register.generator('effigia:gallery-slideshow', GallerySlideshowImage)
register.generator('effigia:gallery-thumbnail', GalleryCoverThumbnail)
register.generator('effigia:portfolio-thumbnail', PortfolioThumbnail)
register.generator('effigia:portfolio-item', PortfolioItemImage)
