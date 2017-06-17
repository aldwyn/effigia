from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<content_type>(gallery|portfolio|post))/(?P<pk>\d+)$',
        views.CommentCreateView.as_view(), name='create'),
]
