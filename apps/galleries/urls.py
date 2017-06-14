from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list$', views.GalleryListView.as_view(), name='list'),
    url(r'^i/(?P<slug>[\w\-]+)$', views.GalleryItemView.as_view(), name='item'),
    url(r'^by-category/(?P<slug>[\w\-]+)$', views.GalleryByCategoryListView.as_view(), name='list-by-category'),
    url(r'^by-user/(?P<slug>[\w\-]+)$', views.GalleryByUserListView.as_view(), name='list-by-user'),
    url(r'^i/(?P<slug>[\w\-]+)/edit$', views.GalleryEditView.as_view(), name='edit'),
    url(r'^i/(?P<slug>[\w\-]+)/delete$', views.GalleryDeleteView.as_view(), name='delete'),
    url(r'^create$', views.GalleryCreateView.as_view(), name='create'),
]
