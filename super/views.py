from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Ask
from .serializers import ProductSerializer, AskSerializer

class ListProduct(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    

class ListAsk(APIView):
    def get(self, request, format=None):
        ask = Ask.objects.filter(show=True)
        serializer = AskSerializer(ask, many=True)
        return Response(serializer.data)