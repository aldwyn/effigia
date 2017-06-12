from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list$', views.CategoryListView.as_view(), name='list'),
]
