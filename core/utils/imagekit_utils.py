from imagekit import ImageSpec
from imagekit.processors import Adjust
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


class GalleryCoverJumbotron(ImageSpec):
    processors = [
        ResizeToFill(940, 400),
        Adjust(contrast=1.2, sharpness=2),
    ]
    format = 'JPEG'
    options = {'quality': 80}


class PortfolioThumbnail(ImageSpec):
    processors = [ResizeToFill(340, 250)]
    format = 'JPEG'
    options = {'quality': 60}


class PortfolioItemImage(ImageSpec):
    processors = [ResizeToFit(700, 500)]
    format = 'JPEG'
    options = {'quality': 60}


class FeedCardThumbnail(ImageSpec):
    processors = [ResizeToFill(40, 40)]
    format = 'JPEG'
    options = {'quality': 60}
