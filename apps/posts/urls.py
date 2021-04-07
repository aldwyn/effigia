from django.urls import path

from . import views


urlpatterns = [
    path('i/<slug>', views.PostItemView.as_view(), name='item'),
    path('i/<slug>/edit', views.PostEditView.as_view(), name='edit'),
    path('g/<slug>/create', views.PostCreateView.as_view(), name='create'),
]
