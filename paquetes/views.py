from django.shortcuts import render
from .models import Paquete

def inicio_paquetes(request):
    return render(request, 'paquetes/inicio.html')

def lista_paquetes(request):
    # Consulta mediante Django ORM
    datos_paquetes = Paquete.objects.select_related('destino').all()
    return render(request, 'paquetes/lista.html', {'paquetes': datos_paquetes})