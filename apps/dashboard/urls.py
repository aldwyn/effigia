from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home$', views.HomeView.as_view(), name='home'),
    url(r'^my-galleries$', views.MyGalleriesView.as_view(), name='my-galleries'),
    url(r'^my-activities$', views.MyActiviesView.as_view(), name='my-activities'),
    url(r'^following$', views.FollowingAllView.as_view(), name='following-all'),
    url(r'^following/galleries$', views.FollowingGalleriesView.as_view(), name='following-galleries'),
    url(r'^following/groups$', views.FollowingGroupsView.as_view(), name='following-groups'),
    url(r'^following/followers$', views.FollowingFollowersView.as_view(), name='following-followers'),
]
