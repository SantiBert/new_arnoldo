from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from caps.urls import caps_patterns, caps_admin_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('', include('social.urls')),
    path('', include(caps_patterns)),
    path('administration/', include(caps_admin_patterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
