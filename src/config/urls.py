from django.contrib import admin
from django.urls import path, include, re_path

from config.schema import schema_view


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls')),
    path('host/', include('host.urls'))
]
