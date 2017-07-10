from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home$', views.HomeView.as_view(), name='home'),
    url(r'^my-galleries$', views.MyGalleriesView.as_view(), name='my-galleries'),
    url(r'^my-activities$', views.MyActiviesView.as_view(), name='my-activities'),
    url(r'^following$', views.FollowingView.as_view(), name='following'),
]
