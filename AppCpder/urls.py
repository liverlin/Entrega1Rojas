
from django.urls import path
from .views import inicio, numero_de_usuario,otra_vista,numero_random, mi_plantilla,probandoTemplate,curso, nuevo_curso
urlpatterns = [
    path('',inicio),
    path('curso',curso),
    path('new-curso',nuevo_curso),
    path('new-view',otra_vista),
    path('random',numero_random),
    path('usuario/<int:numero>',numero_de_usuario),
    path('plantilla',mi_plantilla),
    path('plantilla-dj2',probandoTemplate),
]
