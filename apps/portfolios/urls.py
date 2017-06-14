from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^by-gallery/(?P<slug>[\w\-]+)$', views.PortfolioListView.as_view(), name='list'),
    url(r'^i/(?P<slug>[\w\-]+)$', views.PortfolioItemView.as_view(), name='item'),
    url(r'^i/(?P<slug>[\w\-]+)/edit$', views.PortfolioEditView.as_view(), name='edit'),
    url(r'^i/(?P<slug>[\w\-]+)/delete$', views.PortfolioDeleteView.as_view(), name='delete'),
    url(r'^i/(?P<slug>[\w\-]+)/bulk$', views.PortfolioBulkCreateView.as_view(), name='bulk-create'),
    url(r'^create$', views.PortfolioCreateView.as_view(), name='create'),
]
