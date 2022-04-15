
from django.urls import path
from .views import inicio, numero_de_usuario,otra_vista,numero_random, mi_plantilla,probandoTemplate,curso, nuevo_curso, profesores
from .views import cursos, entregables, estudiantes, inicio_1
urlpatterns = [
    path('',inicio),
    path('curso',curso),
    
    #creados con el ppt
    path('1',inicio_1),
    path('cursos',cursos),
    path('profesores',profesores),
    path('estudiantes',estudiantes),
    path('entregables',entregables),
    
    #sacado de lo de Django
    path('new-curso',nuevo_curso),
    path('new-view',otra_vista),
    path('random',numero_random),
    path('usuario/<int:numero>',numero_de_usuario),
    path('plantilla',mi_plantilla),
    path('plantilla-dj2',probandoTemplate),
]
