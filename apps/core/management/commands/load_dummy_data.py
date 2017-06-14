import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.utils.text import slugify

from apps.categories.models import Category
from apps.comments.factories import CommentFactory
from apps.accounts.factories import UserFactory
from apps.galleries.factories import GalleryFactory
from apps.galleries.models import Gallery
from apps.portfolios.factories import PortfolioFactory
from apps.portfolios.models import Portfolio


User = get_user_model()


class Command(BaseCommand):
    help = 'Loads dummy data'

    def __log_info(self, message):
        self.stdout.write(self.style.NOTICE(message))

    def __log_result(self, data, exists=False):
        res = self.style.WARNING('EXISTS') if exists else self.style.SUCCESS('DONE')
        self.stdout.write('-> "{}"... {}.'.format(data, res))

    def handle(self, *args, **kwargs):
        self.load_dummy_categories()
        self.load_dummy_users()
        self.load_dummy_galleries()
        self.load_dummy_portfolios()
        self.load_dummy_comments()

    def load_dummy_categories(self):
        categories = [
            'Uncategorized', 'Abstract', 'Aerial', 'Animals', 'Black & White', 'Celebrities',
            'City & Architecture', 'Commercial', 'Concert', 'Family', 'Fashion',
            'Film', 'Fine Art', 'Food', 'Journalism', 'Landscape', 'Macro', 'Nature',
            'Night', 'People', 'Performing Arts', 'Sport', 'Still Life', 'Street',
            'Transportation', 'Travel', 'Underwater', 'Urban Exploration', 'Wedding',
        ]
        self.__log_info('Creating {} categories...'.format(len(categories)))
        for c in categories:
            obj, created = Category.objects.get_or_create(name=c, slug=slugify(c))
            self.__log_result(c, not created)
        self.categories = Category.objects.all()

    def load_dummy_users(self, default_user_count=5):
        self.users = User.objects.exclude(username='admin')
        if self.users.count() >= default_user_count:
            self.__log_info('Already created {} users'.format(self.users.count()))
            for user in self.users:
                self.__log_result(user.get_full_name(), exists=True)
        else:
            self.__log_info('Creating {} users...'.format(default_user_count))
            for i in xrange(default_user_count):
                user = UserFactory.create()
                user.save()
                self.__log_result(user.get_full_name())
            self.users = User.objects.exclude(username='admin')

    def load_dummy_galleries(self, default_gallery_count=40):
        self.galleries = Gallery.objects.all()
        if self.galleries.count() >= default_gallery_count:
            self.__log_info('Already created {} galleries'.format(self.galleries.count()))
            for gallery in self.galleries:
                self.__log_result(gallery.name, exists=True)
        else:
            self.__log_info('Creating {} galleries...'.format(default_gallery_count))
            for i in xrange(default_gallery_count):
                gallery = GalleryFactory.create()
                gallery.created_by = random.choice(self.users)
                gallery.category = random.choice(self.categories)
                gallery.save()
                gallery.slug = '{}-{}'.format(slugify(gallery.name), gallery.pk)
                gallery.save()
                for j in xrange(random.randint(1, len(self.users))):
                    gallery.likers.add(random.choice(self.users))

                self.__log_result(gallery.name)
            self.galleries = Gallery.objects.all()

    def load_dummy_portfolios(self, default_portfolio_count=100):
        self.portfolios = Portfolio.objects.all()
        if self.portfolios.count() >= default_portfolio_count:
            self.__log_info('Already created {} portfolios'.format(self.portfolios.count()))
            for portfolio in self.portfolios:
                self.__log_result(portfolio.name, exists=True)
        else:
            self.__log_info('Creating {} portfolios...'.format(default_portfolio_count))
            for i in xrange(default_portfolio_count):
                portfolio = PortfolioFactory.create()
                portfolio.gallery = random.choice(self.galleries)
                portfolio.created_by = portfolio.gallery.created_by
                portfolio.save()
                portfolio.slug = '{}-{}'.format(slugify(portfolio.name), portfolio.pk)
                portfolio.save()
                for j in xrange(random.randint(1, len(self.users))):
                    portfolio.likers.add(random.choice(self.users))
                self.__log_result(portfolio.name)
            self.portfolios = Portfolio.objects.all()

    def load_dummy_comments(self):
        self.__log_info('Creating comments on Galleries...')
        self.__load_comments(self.galleries)
        self.__log_info('Creating comments on Galleries...')
        self.__load_comments(self.portfolios)

    def __load_comments(self, obj_list, default_max_count=15):
        for obj in obj_list:
            counts = random.randint(1, default_max_count)
            self.__log_result('%s: %s comments' % (obj.name, counts))
            for i in xrange(counts):
                comment = CommentFactory.create(
                    content_object=obj,
                    created_by=random.choice(self.users))
                comment.save()
                for j in xrange(random.randint(0, 5)):
                    comment.likers.add(random.choice(self.users))
