from rest_framework import serializers
from .models import Product, Ask


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'thumbnail1', 'thumbnail2', 'thumbnail3', 'thumbnail4', 'thumbnail5', 'video', 'description', 'price', 'supplier', 'release_date']



class AskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ask
        fields = ['id', 'ask', 'description', 'show']
