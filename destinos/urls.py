from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_destinos, name='inicio_destinos'),
    path('lista/', views.lista_destinos, name='lista_destinos'),
]