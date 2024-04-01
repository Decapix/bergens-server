from django.db import models
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models
# Create your models here.



class Client(models.Model):
    """Model for client with 3 PDF files and an ID."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    file1 = models.FileField(upload_to='fichiers/', blank=True, null=True)


class QRCode(models.Model):
    """Model for storing QR codes."""
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='qr_code')
    image = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return f"QR Code for {self.client.name}"

