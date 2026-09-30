from django.db import models
from destinos.models import Destino

class Paquete(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título del Paquete")
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name="paquetes", verbose_name="Destino Asociado")
    noches = models.PositiveIntegerField(verbose_name="Cantidad de Noches")
    precio = models.PositiveIntegerField(verbose_name="Precio ($ CLP)")
    incluye = models.TextField(verbose_name="Servicios Incluidos")

    class Meta:
        verbose_name = "Paquete Turístico"
        verbose_name_plural = "Paquetes Turísticos"

    def __str__(self):
        return f"{self.titulo} - ${self.precio}"