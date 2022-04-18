import imp
from re import template
from django import views
from django.urls import path
#, numero_de_usuario,otra_vista,numero_random, mi_plantilla,probandoTemplate,curso, nuevo_curso, profesores
from .views import buscar, editPerfil, editProf, eliminarProfesor, findCamada, inicio,cursos, estudiantes,profesores, register,showProfesores
#Para CRUD
from .views import CursoList,CursoDetalle,CursoCreacion,CursoDelete,CursoUpdate
#Para Login/out
from .views import login_request
from django.contrib.auth.views import LogoutView

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
    path('editProfesor/<profesor_nombre>/',editProf, name="EditProfesor"),
    
    #CRUD mas simple
    path('AppCpder/curso/list',CursoList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$',CursoDetalle.as_view(),name='Detail'),
    path(r'^nuevo$',CursoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',CursoUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',CursoDelete.as_view(),name='Delete'),
    
    #PPT Avanzado2 LOGIN/OUT
    path('login',login_request, name='Login'),
    path('register',register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCpder/logout.html'),name='Logout'),
    
    #PPT Avanzado3 Edicion de usuario
    path('editarPerfil', editPerfil, name="EditarPerfil"),
]
