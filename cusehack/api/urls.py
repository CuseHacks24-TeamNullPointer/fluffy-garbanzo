from django.contrib import admin
from django.urls import path, include
from api import urls as app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('cusehacks/', include(app_urls)),
]
