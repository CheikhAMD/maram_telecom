from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home





urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('repair/', include('repair.urls')),
    path('', home, name='home'),
    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
