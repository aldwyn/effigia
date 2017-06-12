from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list$', views.GroupListView.as_view(), name='list'),
    url(r'^i/(?P<slug>[\w\-]+)$', views.GroupItemView.as_view(), name='item'),
    url(r'^create$', views.GroupCreateView.as_view(), name='create'),
]
