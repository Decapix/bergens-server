from django.urls import path, include
from client import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('generate_qr/<uuid:client_id>/', views.generate_qr_code, name='generate_qr_code'),
    path("", admin.site.urls),
    path('api/super/', include('super.urls')),
    path('api/client/', include('client.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
