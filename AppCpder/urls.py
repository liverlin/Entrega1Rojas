
from re import template
from django import views
from django.urls import path
#, numero_de_usuario,otra_vista,numero_random, mi_plantilla,probandoTemplate,curso, nuevo_curso, profesores
from .views import buscar, editarPerfil, findCamada, inicio,cursos, register
#Para CRUD
from .views import CursoList,CursoDetalle,CursoCreacion,CursoDelete,CursoUpdate
#Para Login/out
from .views import login_request, user_info, about 
from django.contrib.auth.views import LogoutView

#, inicio_1
urlpatterns = [
    # path('',inicio),
    # path('curso',curso),
    path('', inicio, name="Inicio"),
    path('cursos',cursos,name="Cursos"),

    path('findCamada',findCamada,name="findCamada"),
    path('AppCpder/buscar/',buscar),
    
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
    path('editarPerfil', editarPerfil, name="EditarPerfil"),
    path('info_datos/', user_info, name="user_info"),
    path('about/', about, name="About")
]
