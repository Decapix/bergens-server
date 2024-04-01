from rest_framework import serializers
from .models import Client
from django.conf import settings

class ClientSerializer(serializers.ModelSerializer):
    file1 = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'file1']

    def get_file1(self, obj):
        if obj.file1:
            return f'http://{settings.SERVER_IP}{obj.file1.url}'
        return None
