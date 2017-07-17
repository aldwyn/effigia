from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from apps.accounts.views import ProfileView
from apps.accounts.views import ProfileUpdateView
from apps.accounts.views import SettingsView


urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^', include('apps.dashboard.urls', namespace='dashboard')),
    url(r'^update-profile$', ProfileUpdateView.as_view(), name='account_profile_edit'),
    url(r'^profile/(?P<slug>[\w\-]+)$', ProfileView.as_view(), name='account_profile'),
    url(r'^accounts/settings$', SettingsView.as_view(), name='account_settings'),
    url(r'^chat/', include('apps.chats.urls', namespace='chat')),
    url(r'^interaction/', include('apps.interactions.urls', namespace='interaction')),
    url(r'^gallery/', include('apps.galleries.urls', namespace='gallery')),
    url(r'^group/', include('apps.groups.urls', namespace='group')),
    url(r'^portfolio/', include('apps.portfolios.urls', namespace='portfolio')),
    url(r'^post/', include('apps.posts.urls', namespace='post')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
