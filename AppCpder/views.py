
from django.shortcuts import render

from AppCpder.models import Curso, Estudiante, Profesor
from AppCpder.forms import CursoFormulario, ProfesorFormulario, EstudiantesForm


def inicio(request):
    
    return render(request, "AppCpder/inicio.html",{})


def cursos(request):
    if request.method == 'POST':
        miFormulario= CursoFormulario(request.POST)
        #Aqui me llega toda la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid():#Si paso la validacion de Django
            informacion = miFormulario.cleaned_data
            
            new_curso = Curso(nombre=informacion['curso'],camada=informacion['camada'])
            
            new_curso.save()
            return render(request,"AppCpder/inicio.html",{'new_curso':new_curso}) #Vuelvo al inicio o a donde quieran
    else:
        miFormulario=CursoFormulario()#Formulario vacio para construir el html
        
    return render(request,"AppCpder/cursos.html", {"miFormulario":miFormulario})



def profesores(request):
    if request.method == 'POST':
        miFormulario= ProfesorFormulario(request.POST)#Aqui me llega toda la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:#Si paso la validacion de Django
            informacion = miFormulario.cleaned_data
            
            new_profesor = Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],
                             email=informacion['email'],profesion=informacion['profesion'])
            
            new_profesor.save()
            return render(request,"AppCpder/inicio.html",{'profesor':new_profesor}) #Vuelvo al inicio o a donde quieran
    
    else:
        miFormulario=ProfesorFormulario()#Formulario vacio para construir el html
        
    return render(request,"AppCpder/profesores.html", {"miFormulario":miFormulario})


def estudiantes(request):
    if request.method == 'POST':
        miFormulario= EstudiantesForm(request.POST)#Aqui me llega toda la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:#Si paso la validacion de Django
            informacion = miFormulario.cleaned_data
            
            new_estudiante = Estudiante(nombre=informacion['nombre'],apellido=informacion['apellido'],
                             email=informacion['email'])
            
            new_estudiante.save()
            return render(request,"AppCpder/inicio.html",{'profesor':new_estudiante}) #Vuelvo al inicio o a donde quieran
    
    else:
        miFormulario=ProfesorFormulario()#Formulario vacio para construir el html
        
    return render(request,"AppCpder/estudiantes.html", {"miFormulario":miFormulario})



def findCamada(request):
    
    return render(request, "AppCpder/findCamada.html")


def buscar(request):
    if request.GET["camada"]:#si envio un dato de camada
        
        camada=request.GET['camada'] #lo guardo en variabe camada
        #tbm se puede buscar con get
        cursos_buscados = Curso.objects.filter(camada__icontains=camada)
        #almaceno las respuestas en la variables cursos
        
        return render(request,"AppCpder/inicio.html",{"cursos":cursos_buscados,"camada":camada})
    else:
        respuesta="No enviaste datos"
    
    return render(request, "AppCpder/inicio.html", {"respuesta":respuesta})
    