from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer
from django.http import HttpResponseRedirect
from django.contrib import admin
from .models import Client, QRCode
import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from rest_framework import status
from django.http import HttpResponse, Http404


class ClientFilesAPIView(APIView):
    def get(self, request, client_id, format=None):
        try:
            client = Client.objects.get(id=client_id)
            if client.file1:
                with open(client.file1.path, 'rb') as pdf:
                    response = HttpResponse(pdf.read(), content_type='application/pdf')
                    response['Content-Disposition'] = f'inline; filename={client.file.name}'
                    return response
            else:
                return HttpResponse('No PDF file found.', status=404)
        except Client.DoesNotExist:
            return Http404("Client not found")




def generate_qr_code(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    qr_code_instance, created = QRCode.objects.get_or_create(client=client)
    
    if created or not qr_code_instance.image:  # Utiliser 'image' au lieu de 'qr_code'
        # Générer l'URL
        url = f'{settings.DOMAIN_FRONT}/client/{client.id}'

        # Générer le QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        filename = f'{client.id}.png'

        # Sauvegarder l'image QR code dans le champ 'image' du modèle QRCode
        qr_code_instance.image.save(filename, File(buffer), save=True)

    return redirect(request.META.get('HTTP_REFERER', 'admin:index'))
