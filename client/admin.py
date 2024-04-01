from django.utils.html import format_html
from django.contrib import admin
from .models import Client, QRCode

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file1', 'qr_code_link']

    def qr_code_link(self, obj):
        qr_code = QRCode.objects.filter(client=obj).first()
        if qr_code:
            return format_html(f'<a href="{qr_code.image.url}">Afficher</a>')
        return format_html(f'<a href="/admin/generate_qr/{obj.id}">Générer</a>')

    qr_code_link.short_description = 'QR Code'

    def has_change_permission(self, request, obj=None):
        return False if obj is None else True


admin.site.register(QRCode)

