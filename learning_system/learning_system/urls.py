from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('study/', include('study.urls')),
    path('catalog/', include('catalog.urls'))
]
