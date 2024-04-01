from django.db import models
import uuid


class Product(models.Model):
    """Model for product"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    thumbnail1 = models.ImageField(upload_to='products/', blank=True)
    thumbnail2 = models.ImageField(upload_to='products/', blank=True)
    thumbnail3 = models.ImageField(upload_to='products/', blank=True)
    thumbnail4 = models.ImageField(upload_to='products/', blank=True)
    thumbnail5 = models.ImageField(upload_to='products/', blank=True)
    video = models.FileField(upload_to='products/videos/', blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supplier = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)




class Ask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ask = models.TextField(max_length=360)
    description = models.TextField(max_length=4000)
    show = models.BooleanField()

    def __str__(self):
        return f"{self.ask}"