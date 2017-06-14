from django.conf.urls import url

from .views import LoginView
from .views import LogoutView
from .views import RegistrationView
from .views import ProfileView


urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^register/', RegistrationView.as_view(), name='register'),
    url(r'^profile/', ProfileView.as_view(), name='profile'),
]
