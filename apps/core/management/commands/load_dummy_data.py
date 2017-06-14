import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.utils.text import slugify

from apps.categories.models import Category
from apps.comments.models import Comment
from apps.accounts.factories import UserFactory
from apps.galleries.factories import GalleryFactory
from apps.galleries.models import Gallery
from apps.portfolios.factories import PortfolioFactory
from apps.portfolios.models import Portfolio


User = get_user_model()


class Command(BaseCommand):
    help = 'Loads dummy data'

    def log_info(self, message):
        self.stdout.write(self.style.NOTICE(message))

    def log_result(self, data, exists=False):
        res = self.style.WARNING('EXISTS') if exists else self.style.SUCCESS('DONE')
        self.stdout.write('-> "{}"... {}.'.format(data, res))

    def handle(self, *args, **kwargs):
        categories = [
            'Uncategorized', 'Abstract', 'Aerial', 'Animals', 'Black & White', 'Celebrities',
            'City & Architecture', 'Commercial', 'Concert', 'Family', 'Fashion',
            'Film', 'Fine Art', 'Food', 'Journalism', 'Landscape', 'Macro', 'Nature',
            'Night', 'People', 'Performing Arts', 'Sport', 'Still Life', 'Street',
            'Transportation', 'Travel', 'Underwater', 'Urban Exploration', 'Wedding',
        ]

        self.log_info('Creating {} categories...'.format(len(categories)))
        for c in categories:
            obj, created = Category.objects.get_or_create(name=c, slug=slugify(c))
            self.log_result(c, not created)
        categories = Category.objects.all()

        default_user_count = 5
        users = User.objects.exclude(username='admin')
        if users.count() >= default_user_count:
            self.log_info('Already created {} users'.format(users.count()))
            for user in users:
                self.log_result(user.get_full_name(), exists=True)
        else:
            self.log_info('Creating {} users...'.format(default_user_count))
            for i in xrange(default_user_count):
                user = UserFactory.create()
                user.save()
                self.log_result(user.get_full_name())
            users = User.objects.exclude(username='admin')

        default_gallery_count = 40
        galleries = Gallery.objects.all()
        if galleries.count() >= default_gallery_count:
            self.log_info('Already created {} galleries'.format(galleries.count()))
            for gallery in galleries:
                self.log_result(gallery.name, exists=True)
        else:
            self.log_info('Creating {} galleries...'.format(default_gallery_count))
            for i in xrange(default_gallery_count):
                gallery = GalleryFactory.create()
                gallery.created_by = random.choice(users)
                gallery.category = random.choice(categories)
                gallery.save()
                gallery.slug = '{}-{}'.format(slugify(gallery.name), gallery.pk)
                gallery.save()
                for j in xrange(random.randint(1, len(users))):
                    gallery.likers.add(random.choice(users))
                self.log_result(gallery.name)
            galleries = Gallery.objects.all()

        default_portfolio_count = 100
        portfolios = Portfolio.objects.all()
        if portfolios.count() >= default_portfolio_count:
            self.log_info('Already created {} portfolios'.format(portfolios.count()))
            for portfolio in portfolios:
                self.log_result(portfolio.name, exists=True)
        else:
            self.log_info('Creating {} portfolios...'.format(default_portfolio_count))
            for i in xrange(default_portfolio_count):
                portfolio = PortfolioFactory.create()
                portfolio.gallery = random.choice(galleries)
                portfolio.created_by = portfolio.gallery.created_by
                portfolio.save()
                portfolio.slug = '{}-{}'.format(slugify(portfolio.name), portfolio.pk)
                portfolio.save()
                for j in xrange(random.randint(1, len(users))):
                    portfolio.likers.add(random.choice(users))
                self.log_result(portfolio.name)
            portfolios = Portfolio.objects.all()
