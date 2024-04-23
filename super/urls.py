from django.urls import path
from .views import ListProduct, ListAsk

urlpatterns = [
    path('product/', ListProduct.as_view(), name='listproduct'),
    path('ask/', ListAsk.as_view(), name='listask'),

]
