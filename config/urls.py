from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^', include('apps.dashboard.urls', namespace='dashboard')),
    url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),
    url(r'^category/', include('apps.categories.urls', namespace='category')),
    url(r'^gallery/', include('apps.galleries.urls', namespace='gallery')),
    url(r'^portfolio/', include('apps.portfolios.urls', namespace='portfolio')),
    url(r'^group/', include('apps.groups.urls', namespace='group')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
