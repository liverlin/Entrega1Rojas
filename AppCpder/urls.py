
from django import views
from django.urls import path
#, numero_de_usuario,otra_vista,numero_random, mi_plantilla,probandoTemplate,curso, nuevo_curso, profesores
from .views import buscar, editProf, eliminarProfesor, findCamada, inicio,cursos, estudiantes,profesores,showProfesores
#, inicio_1
urlpatterns = [
    # path('',inicio),
    # path('curso',curso),
    path('', inicio, name="Inicio"),
    path('cursos',cursos,name="Cursos"),
    path('profesores',profesores,name="Profesores"),
    path('estudiantes',estudiantes,name="Estudiantes"),
    path('findCamada',findCamada,name="findCamada"),
    path('AppCpder/buscar/',buscar),
    #CRUD Básico
    path('showProfesores',showProfesores,name="showProfesores"),
    path('eliminarProfesor/<profesor_nombre>/',eliminarProfesor, name="EliminarProfesor"),
    #comenta ps
    path('editProfesor/<profesor_nombre>/',editProf, name="EditProfesor"),
    #CRUD mas simple
    
    path('showcursos/',views.CursoList.as_view(),name="profesor_list")
    
    
]
