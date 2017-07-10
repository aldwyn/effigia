from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^i/(?P<slug>[\w\-]+)$', views.PostItemView.as_view(), name='item'),
    url(r'^i/(?P<slug>[\w\-]+)/edit$', views.PostEditView.as_view(), name='edit'),
    url(r'^g/(?P<slug>[\w\-]+)/create$', views.PostCreateView.as_view(), name='create'),
]
