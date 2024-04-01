from django.urls import path
from .views import ListProduct, ListAsk

urlpatterns = [
    path('api/product/', ListProduct.as_view(), name='listproduct'),
    path('api/ask/', ListAsk.as_view(), name='listask'),

]
