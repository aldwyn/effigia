from django.urls import path

from . import views


urlpatterns = [
    path('list', views.GroupListView.as_view(), name='list'),
    path('i/<slug>/', views.GroupItemView.as_view(), name='item'),
    path('create', views.GroupCreateView.as_view(), name='create'),
]
