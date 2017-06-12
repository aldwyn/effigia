from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list$', views.GalleryListView.as_view(), name='list'),
    url(r'^i/(?P<slug>[\w\-]+)$', views.GalleryItemView.as_view(), name='item'),
    url(r'^i/(?P<slug>[\w\-]+)/edit$', views.GalleryEditView.as_view(), name='edit'),
    url(r'^i/(?P<slug>[\w\-]+)/delete$', views.GalleryDeleteView.as_view(), name='delete'),
    url(r'^create$', views.GalleryCreateView.as_view(), name='create'),
]
