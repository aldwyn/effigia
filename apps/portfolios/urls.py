from django.urls import path

from . import views


urlpatterns = [
    path('by-gallery/<slug>', views.PortfolioListView.as_view(), name='list'),
    path('i/<slug>', views.PortfolioItemView.as_view(), name='item'),
    path('i/<slug>/edit', views.PortfolioEditView.as_view(), name='edit'),
    path('i/<slug>/delete', views.PortfolioDeleteView.as_view(), name='delete'),
    path('i/<slug>/bulk', views.PortfolioBulkCreateView.as_view(), name='bulk-create'),
    path('create', views.PortfolioCreateView.as_view(), name='create'),
]
