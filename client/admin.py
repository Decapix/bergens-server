from django.utils.html import format_html
from django.contrib import admin
from .models import Client, QRCode

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file1', 'get_link', 'qr_code_link']
    change_form_template = 'admin/client_change_form.html'

    def qr_code_link(self, obj):
        qr_code = QRCode.objects.filter(client=obj).first()
        if qr_code:
            return format_html(f'<a href="{qr_code.image.url}">Afficher</a>')
        return format_html(f'<a href="/admin/generate_qr/{obj.id}">Générer</a>')

    qr_code_link.short_description = 'QR Code'



    def get_link(self, obj):
        # Bouton qui appelle une fonction JavaScript pour copier l'URL dans le presse-papier
        return format_html(
            '<button onclick="copyToClipboard(\'{}\')">Copier le lien</button>',
            f'https://admin.bergens.fr/api/client/{obj.id}'
        )
    

    get_link.short_description = 'Copier le lien'

    def has_change_permission(self, request, obj=None):
        return False if obj is None else True


admin.site.register(QRCode)

