from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("dashboard.urls")),
    path('account/', include("account.urls")),
    path('api/', include("api.urls")),
]

admin.site.site_header = "CHURCH - DATABASE ADMINISTRATOR"
admin.site.index_title = "TABLES"                   
admin.site.site_title =  'Super User'               


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)