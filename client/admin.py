from django.utils.html import format_html
from django.contrib import admin
from .models import Client, QRCode

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'Seq_nr', 'name', 'file1', 'get_link', 'qr_code_link']

    def get_link(self, obj):
        # Utiliser un attribut data-url pour stocker l'URL et une classe spécifique pour le bouton
        url = f'https://admin.bergens.fr/api/client/{obj.id}'
        return format_html('<button data-url="{0}" class="copy-btn">Copier le lien</button>', url)

    get_link.short_description = 'Copier le lien'

    def qr_code_link(self, obj):
        qr_code = QRCode.objects.filter(client=obj).first()
        if qr_code:
            return format_html('<a href="{0}">Afficher</a>', qr_code.image.url)
        return format_html('<a href="/admin/generate_qr/{0}">Générer</a>', obj.id)

    qr_code_link.short_description = 'QR Code'

    def has_change_permission(self, request, obj=None):
        return False if obj is None else True

    class Media:
        js = ('js/admin_custom.js',)


admin.site.register(QRCode)

