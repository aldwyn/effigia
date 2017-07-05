import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from apps.categories.models import Category
from apps.interactions.factories import CommentFactory
from apps.interactions.models import Comment
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
        self.load_dummy_categories()
        self.load_dummy_users()
        self.load_dummy_galleries()
        self.load_dummy_portfolios()
        self.load_dummy_groups()
        self.load_dummy_posts()
        self.load_dummy_comments(self.galleries)
        self.load_dummy_comments(self.portfolios)
        self.load_dummy_comments(self.posts)

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
        users = []
        for i in xrange(default_user_count):
            user = UserFactory.create()
            users.append(user)
            self.__log_result(user.get_full_name())
        User.objects.bulk_create(users)
        self.users = User.objects.exclude(username='admin')

    def load_dummy_galleries(self, default_gallery_count=40):
        self.__log_info('Creating {} galleries...'.format(default_gallery_count))
        galleries = []
        for i in xrange(default_gallery_count):
            gallery = GalleryFactory.create(
                created_by=random.choice(self.users),
                category=random.choice(self.categories),
                slug='gallery-%s' % i,
            )
            galleries.append(gallery)
            self.__log_result(gallery.name)
        Gallery.objects.bulk_create(galleries)
        self.galleries = Gallery.objects.all()
        # self.__log_info('Creating random likers on Galleries...')
        # for gallery in self.galleries:
        #     gallery.likers.add(
        #         *random.sample(self.users, random.randint(1, len(self.users))))

    def load_dummy_portfolios(self, default_portfolio_count=100):
        self.__log_info('Creating {} portfolios...'.format(default_portfolio_count))
        portfolios = []
        for i in xrange(default_portfolio_count):
            gallery = random.choice(self.galleries)
            portfolio = PortfolioFactory.create(
                gallery=gallery,
                created_by=gallery.created_by,
                slug='portfolio-%s' % i
            )
            portfolios.append(portfolio)
            self.__log_result(portfolio.name)
        Portfolio.objects.bulk_create(portfolios)
        self.portfolios = Portfolio.objects.all()
        # self.__log_info('Creating random likers on Portfolios...')
        # for portfolio in self.portfolios:
        #     portfolio.likers.add(
        #         *random.sample(self.users, random.randint(1, len(self.users))))

    def load_dummy_groups(self, default_group_count=30):
        self.__log_info('Creating {} groups...'.format(default_group_count))
        groups = []
        for i in xrange(default_group_count):
            group = GroupFactory.create(
                created_by=random.choice(self.users),
                slug='group-%s' % i
            )
            groups.append(group)
            self.__log_result(group.name)
        Group.objects.bulk_create(groups)
        self.groups = Group.objects.all()
        # for group in self.groups:
        #     group.members.add(
        #         *random.sample(self.users, random.randint(1, len(self.users))))

    def load_dummy_posts(self, default_post_count=500):
        self.__log_info('Creating {} posts...'.format(default_post_count))
        posts = []
        for i in xrange(default_post_count):
            post = PostFactory.create(
                group=random.choice(self.groups),
                created_by=random.choice(self.users),
            )
            posts.append(post)
            self.__log_result(post.text[:50])
        Post.objects.bulk_create(posts)
        self.posts = Post.objects.all()
        # for posts in self.posts:
        #     posts.likers.add(
        #         *random.sample(self.users, random.randint(1, len(self.users))))

    def load_dummy_comments(self, obj_list, default_max_count=15):
        self.__log_info('Creating comments on `{}`...'.format(obj_list[0].__class__))
        comments_pool = [CommentFactory.create() for _ in xrange(100)]
        comments_batch = []
        for obj in obj_list:
            counts = random.randint(1, default_max_count)
            self.__log_result('%s: %s comments' % (obj, counts))
            for comment in random.sample(comments_pool, counts):
                comment.content_object = obj
                comment.created_by = random.choice(self.users)
                comments_batch.append(comment)
        Comment.objects.bulk_create(comments_batch)
        # self.__log_info('Creating random likers on Comments...')
        # for obj in obj_list:
        #     for comment in obj.comments.all():
        #         comment.likers.add(
        #             *random.sample(self.users, random.randint(0, len(self.users))))
