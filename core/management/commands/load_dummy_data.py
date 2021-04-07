import random

from actstream.actions import follow
from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.models import Category
from core.models import Quote
from apps.interactions.factories import CommentFactory
from apps.accounts.factories import UserFactory
from apps.galleries.factories import GalleryFactory
from apps.galleries.models import Gallery
from apps.portfolios.factories import PortfolioFactory
from apps.portfolios.models import Portfolio
from apps.groups.models import Group
from apps.groups.factories import GroupFactory
from apps.posts.models import Post
from apps.posts.factories import PostFactory


User = get_user_model()


class Command(BaseCommand):
    help = 'Loads dummy data'

    def __log_info(self, message):
        self.stdout.write(self.style.NOTICE(message))

    def __log_result(self, data, exists=False):
        res = self.style.WARNING('EXISTS') if exists else self.style.SUCCESS('QUEUED')
        self.stdout.write('-> "{}"... {}.'.format(data, res))

    def handle(self, *args, **kwargs):
        self.load_social_providers()
        self.load_dummy_categories()

        # Create superuser
        admin = User(username='admin',
                     email='admin@effigia.com',
                     is_superuser=True,
                     is_staff=True)
        admin.set_password(settings.DJANGO_ADMIN_PASS)
        admin.save()

        self.load_quotes()
        self.load_dummy_users()
        self.load_dummy_galleries()
        self.load_dummy_portfolios()
        self.load_dummy_groups()
        self.load_dummy_posts()
        self.load_dummy_comments(self.galleries)
        self.load_dummy_comments(self.portfolios)
        self.load_dummy_comments(self.posts)
        self.load_dummy_followings(self.users)
        self.load_dummy_followings(self.galleries)
        self.load_dummy_followings(self.groups)
        self.__log_info('LOADING DUMMY DATA: FINISHED.')

    def load_social_providers(self):
        current_site = Site.objects.get_current()
        current_site.domain = 'effigia.com'
        current_site.name = 'Effigia'
        current_site.save()
        google_app = SocialApp.objects.create(
            name='Google',
            provider='google',
            client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
            secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET)
        facebook_app = SocialApp.objects.create(
            name='Facebook',
            provider='facebook',
            client_id=settings.FACEBOOK_OAUTH2_CLIENT_ID,
            secret=settings.FACEBOOK_OAUTH2_CLIENT_SECRET)
        twitter_app = SocialApp.objects.create(
            name='Twitter',
            provider='twitter',
            client_id=settings.TWITTER_OAUTH2_CLIENT_ID,
            secret=settings.TWITTER_OAUTH2_CLIENT_SECRET)
        google_app.sites.add(current_site)
        facebook_app.sites.add(current_site)
        twitter_app.sites.add(current_site)

    def load_dummy_categories(self):
        categories = [
            'Uncategorized', 'Abstract', 'Aerial', 'Animals', 'Black & White', 'Celebrities',
            'City & Architecture', 'Commercial', 'Concert', 'Family', 'Fashion',
            'Film', 'Fine Art', 'Food', 'Journalism', 'Landscape', 'Macro', 'Nature',
            'Night', 'People', 'Performing Arts', 'Sport', 'Still Life', 'Street',
            'Transportation', 'Travel', 'Underwater', 'Urban Exploration', 'Wedding',
        ]
        self.__log_info('Creating {} categories...'.format(len(categories)))
        category_objs = []
        for c in categories:
            category_objs.append(Category(name=c, slug=slugify(c)))
            self.__log_result(c)
        Category.objects.bulk_create(category_objs)
        self.categories = Category.objects.all()

    def load_dummy_users(self, default_user_count=30):
        self.__log_info('Creating {} users...'.format(default_user_count))
        for i in range(default_user_count):
            user = UserFactory.build()
            user.save()
            user.profile.is_test_user = True
            user.profile.save()
            self.__log_result(user.get_full_name())
        self.users = User.objects.exclude(username='admin')

    def load_dummy_galleries(self, default_gallery_count=40):
        self.__log_info('Creating {} galleries...'.format(default_gallery_count))
        for i in range(default_gallery_count):
            gallery = GalleryFactory.build(
                created_by=random.choice(self.users),
                category=random.choice(self.categories),
                slug='gallery-%s' % i,
            )
            gallery.save()
            self.__log_result(gallery.name)
        self.galleries = Gallery.objects.exclude(is_default=True)

    def load_dummy_portfolios(self, default_portfolio_count=100):
        self.__log_info('Creating {} portfolios...'.format(default_portfolio_count))
        for i in range(default_portfolio_count):
            gallery = random.choice(self.galleries)
            portfolio = PortfolioFactory.build(
                gallery=gallery,
                created_by=gallery.created_by,
                slug='portfolio-%s' % i
            )
            self.__log_result(portfolio.name)
            portfolio.save()
        self.portfolios = Portfolio.objects.all()

    def load_dummy_groups(self, default_group_count=30):
        self.__log_info('Creating {} groups...'.format(default_group_count))
        for i in range(default_group_count):
            group = GroupFactory.build(
                created_by=random.choice(self.users),
                slug='group-%s' % i
            )
            self.__log_result(group.name)
            group.save()
        self.groups = Group.objects.all()

    def load_dummy_posts(self, default_post_count=100):
        self.__log_info('Creating {} posts...'.format(default_post_count))
        for i in range(default_post_count):
            post = PostFactory.build(
                group=random.choice(self.groups),
                created_by=random.choice(self.users),
                slug='post-%s' % i,
            )
            self.__log_result(post.name)
            post.save()
        self.posts = Post.objects.all()

    def load_dummy_comments(self, obj_list, default_max_count=15):
        self.__log_info('Creating comments on `{}`...'.format(obj_list[0].__class__))
        comments_pool = [CommentFactory.build() for _ in range(100)]
        for obj in obj_list:
            counts = random.randint(1, default_max_count)
            self.__log_result('%s: %s comments' % (obj, counts))
            for comment in random.sample(comments_pool, counts):
                comment.content_object = obj
                comment.created_by = random.choice(self.users)
                comment.save()

    def load_dummy_followings(self, obj_list, default_max_count=10):
        self.__log_info('Creating followings on `{}`...'.format(obj_list[0].__class__))
        for user in self.users:
            for obj in random.sample(list(obj_list), random.randint(1, default_max_count)):
                if obj != user:
                    follow(user, obj)

    def load_quotes(self, max_len=1000):
        self.__log_info('Loading {} random quotes ...'.format(max_len))
        with open('core/resources/quotes.txt') as f:
            quote_lines = f.readlines()[:max_len]
            quotes = []
            for quote in random.sample(quote_lines, max_len):
                author, text = quote.split('\t', 1)
                quotes.append(Quote(text=text.strip(), author=author))
            Quote.objects.bulk_create(quotes)
