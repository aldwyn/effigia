from django.urls import path

from . import views


urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('my-galleries', views.MyGalleriesView.as_view(), name='my-galleries'),
    path('my-activities', views.MyActiviesView.as_view(), name='my-activities'),
    path('feeds', views.FeedsAllView.as_view(), name='feeds-all'),
    path('feeds/galleries', views.FeedsGalleriesView.as_view(), name='feeds-galleries'),
    path('feeds/groups', views.FeedsGroupsView.as_view(), name='feeds-groups'),
    path('followings', views.FollowingsUsersView.as_view(), name='followings-users'),
    path('followings/galleries', views.FollowingsGalleriesView.as_view(), name='followings-galleries'),
    path('followings/groups', views.FollowingsGroupsView.as_view(), name='followings-groups'),
    path('followings/followers', views.FollowingsFollowersView.as_view(), name='followings-followers'),
]
