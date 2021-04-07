from django.urls import path

from . import views


urlpatterns = [
    path('list', views.GalleryListView.as_view(), name='list'),
    path('i/<slug>', views.GalleryItemView.as_view(), name='item'),
    path('by-category/<slug>', views.GalleryByCategoryListView.as_view(), name='list-by-category'),
    path('i/<slug>/edit', views.GalleryEditView.as_view(), name='edit'),
    path('i/<slug>/delete', views.GalleryDeleteView.as_view(), name='delete'),
    path('create', views.GalleryCreateView.as_view(), name='create'),
]
