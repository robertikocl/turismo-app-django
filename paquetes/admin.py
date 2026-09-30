from django.contrib import admin
from .models import Paquete

@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'destino', 'noches', 'precio')
    search_fields = ('titulo', 'incluye', 'destino__nombre')
    list_filter = ('destino', 'noches')