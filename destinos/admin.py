from django.contrib import admin
from .models import Region, Destino

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'zona')
    search_fields = ('nombre', 'zona')

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'region', 'imagen')
    search_fields = ('nombre', 'descripcion', 'region__nombre')
    list_filter = ('region',)