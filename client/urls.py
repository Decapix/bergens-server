
from django.urls import path
from .views import ClientFilesAPIView

urlpatterns = [
    path('api/<uuid:client_id>/', ClientFilesAPIView.as_view(), name='client-files-api'),
    # Incluez vos autres URL ici...
]
