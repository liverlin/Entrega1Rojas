
from re import template
from django import views
from django.urls import path
from .views import editProf, eliminarProfesor, estudiantes,profesores,showProfesores,showEstudiantes


from django.contrib.auth.views import LogoutView

#, inicio_1
urlpatterns = [
    path('profesores',profesores,name="Profesores"),
    path('estudiantes',estudiantes,name="Estudiantes"),
    
    #CRUD Básico
    path('showEstudents', showEstudiantes, name="showEstudiantes"),
    
    path('showProfesores',showProfesores,name="showProfesores"),
    path('eliminarProfesor/<profesor_nombre>/',eliminarProfesor, name="EliminarProfesor"),
    path('editProfesor/<profesor_nombre>/',editProf, name="EditProfesor"),

]
