"""miproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import inicio, numero_de_usuario,otra_vista,numero_random, mi_plantilla,probandoTemplate
from AppCpder.views import curso

urlpatterns = [
    path('',inicio),
    path('curso',curso),
    path('new-view',otra_vista),
    path('random',numero_random),
    path('usuario/<int:numero>',numero_de_usuario),
    path('plantilla',mi_plantilla),
    path('plantilla-dj2',probandoTemplate),
    path('admin/', admin.site.urls),
]