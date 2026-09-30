from django.shortcuts import render
from .models import Destino

def inicio_destinos(request):
    return render(request, 'destinos/inicio.html')

def lista_destinos(request):
    # Consulta ORM a la base de datos trayendo la relación con Región
    datos_destinos = Destino.objects.select_related('region').all()
    return render(request, 'destinos/lista.html', {'destinos': datos_destinos})