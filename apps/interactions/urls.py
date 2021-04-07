from django.urls import path
from django.urls import re_path

from . import views


urlpatterns = [
    path('join-group/<slug>', views.JoinGroupCreateView.as_view(), name='join-group'),
    path('leave-group/<slug>', views.LeaveGroupCreateView.as_view(), name='leave-group'),
    re_path('^follow/(?P<content_type>(gallery|user))/(?P<pk>\d+)$',
        views.FollowingCreateView.as_view(), name='follow'),
    re_path('^like/(?P<content_type>(gallery|post|portfolio|comment))/(?P<pk>\d+)$',
        views.LikeCreateView.as_view(), name='like-create'),
    re_path('^comment/(?P<content_type>(gallery|portfolio|post))/(?P<pk>\d+)$',
        views.CommentCreateView.as_view(), name='comment-create'),
    re_path('^unfollow/(?P<content_type>(gallery|user))/(?P<pk>\d+)$',
        views.FollowingDeleteView.as_view(), name='unfollow'),
    path('like/<int:pk>/delete', views.LikeDeleteView.as_view(), name='like-delete'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='comment-delete'),
]
