from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('destinos/', include('destinos.urls')),
    path('paquetes/', include('paquetes.urls')),
]