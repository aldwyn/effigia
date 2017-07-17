from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home$', views.HomeView.as_view(), name='home'),
    url(r'^my-galleries$', views.MyGalleriesView.as_view(), name='my-galleries'),
    url(r'^my-activities$', views.MyActiviesView.as_view(), name='my-activities'),
    url(r'^feeds$', views.FeedsAllView.as_view(), name='feeds-all'),
    url(r'^feeds/galleries$', views.FeedsGalleriesView.as_view(), name='feeds-galleries'),
    url(r'^feeds/groups$', views.FeedsGroupsView.as_view(), name='feeds-groups'),
    url(r'^followings$', views.FollowingsUsersView.as_view(), name='followings-users'),
    url(r'^followings/galleries$', views.FollowingsGalleriesView.as_view(), name='followings-galleries'),
    url(r'^followings/groups$', views.FollowingsGroupsView.as_view(), name='followings-groups'),
    url(r'^followings/followers$', views.FollowingsFollowersView.as_view(), name='followings-followers'),
]
