from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('api.urls')),
]

if settings.DEBUG:

    from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView)

    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
        path("swagger/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),
        path('redoc/', SpectacularRedocView.as_view(url_name='api-schema'), name='redoc'),
    ]
