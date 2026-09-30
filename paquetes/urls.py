from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_paquetes, name='inicio_paquetes'),
    path('lista/', views.lista_paquetes, name='lista_paquetes'),
]