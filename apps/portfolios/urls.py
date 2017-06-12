from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^g/(?P<slug>[\w\-]+)$', views.PortfolioListView.as_view(), name='list'),
    url(r'^i/(?P<slug>[\w\-]+)$', views.PortfolioItemView.as_view(), name='item'),
    url(r'^create$', views.PortfolioCreateView.as_view(), name='create'),
]
