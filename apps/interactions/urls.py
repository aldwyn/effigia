from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^join-group/(?P<slug>[\w\-]+)$', views.JoinGroupCreateView.as_view(), name='join-group'),
    url(r'^leave-group/(?P<slug>[\w\-]+)$', views.LeaveGroupCreateView.as_view(), name='leave-group'),
    url(r'^follow/(?P<content_type>(gallery|user))/(?P<pk>\d+)$',
        views.FollowingCreateView.as_view(), name='follow'),
    url(r'^like/(?P<content_type>(gallery|post|portfolio|comment))/(?P<pk>\d+)$',
        views.LikeCreateView.as_view(), name='like-create'),
    url(r'^comment/(?P<content_type>(gallery|portfolio|post))/(?P<pk>\d+)$',
        views.CommentCreateView.as_view(), name='comment-create'),
    url(r'^unfollow/(?P<content_type>(gallery|user))/(?P<pk>\d+)$',
        views.FollowingDeleteView.as_view(), name='unfollow'),
    url(r'^like/(?P<pk>\d+)/delete$', views.LikeDeleteView.as_view(), name='like-delete'),
    url(r'^comment/(?P<pk>\d+)/delete$', views.CommentDeleteView.as_view(), name='comment-delete'),
]
