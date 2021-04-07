from django.conf import settings
from django.conf.urls import include
from django.urls.conf import path
from django.conf.urls.static import static
from django.contrib import admin

from apps.accounts.views import ProfileView
from apps.accounts.views import ProfileUpdateView
from apps.accounts.views import SettingsView


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('django_prometheus.urls')),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('', include(('apps.dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('update-profile', ProfileUpdateView.as_view(), name='account_profile_edit'),
    path('profile/<slug>', ProfileView.as_view(), name='account_profile'),
    path('accounts/settings', SettingsView.as_view(), name='account_settings'),
    path('chat/', include(('apps.chats.urls', 'chat'), namespace='chat')),
    path('interaction/', include(('apps.interactions.urls', 'interaction'), namespace='interaction')),
    path('gallery/', include(('apps.galleries.urls', 'gallery'), namespace='gallery')),
    path('group/', include(('apps.groups.urls', 'group'), namespace='group')),
    path('portfolio/', include(('apps.portfolios.urls', 'portfolio'), namespace='portfolio')),
    path('post/', include(('apps.posts.urls', 'post'), namespace='post')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
