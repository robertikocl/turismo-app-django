from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Región")
    zona = models.CharField(max_length=50, verbose_name="Zona Geográfica (Ej: Norte Chico)")

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.nombre

class Destino(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Ciudad o Destino")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="destinos", verbose_name="Región")
    descripcion = models.TextField(verbose_name="Descripción Turística")
    imagen = models.CharField(max_length=100, help_text="Ej: serena.jpg o vallenar.jpg", verbose_name="Archivo de Imagen")

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"

    def __str__(self):
        return f"{self.nombre} ({self.region.nombre})"