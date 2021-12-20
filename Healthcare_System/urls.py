from django import contrib
from django.contrib import admin
from django.urls import conf, path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicine.urls')),
    path('manufacturers/', include('manufacturer.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
