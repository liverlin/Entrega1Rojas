
from django.shortcuts import redirect, render

from django.urls import reverse_lazy

#Decorador por defecto
from django.contrib.auth.decorators import login_required


from Aula.models import Estudiante, Profesor
from Aula.forms import ProfesorFormulario, EstudiantesForm
# Create your views here.

def profesores(request):
    if request.method == 'POST':
        miFormulario= ProfesorFormulario(request.POST)#Aqui me llega toda la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:#Si paso la validacion de Django
            informacion = miFormulario.cleaned_data
            
            new_profesor = Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],
                email=informacion['email'],profesion=informacion['profesion'])
            
            new_profesor.save()
            #return render(request,"Aula/inicio.html",{'profesor':new_profesor}) #Vuelvo al inicio o a donde quieran
            return render(request,"AppCpder/inicio.html") #Vuelvo al inicio o a donde quieran
    
    else:
        miFormulario=ProfesorFormulario()#Formulario vacio para construir el html
        
    return render(request,"Aula/profesores.html", {"miFormulario":miFormulario})


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
        miFormulario=EstudiantesForm()#Formulario vacio para construir el html
        
    return render(request,"Aula/estudiantes.html", {"miFormulario":miFormulario})

def showEstudiantes(request):
    estudiantes = Estudiante.objects.all() #trae todos los profesores creados
    contexto={"estudiantes":estudiantes}
    
    return render(request, "Aula/leerEstudiantes.html",contexto)

def showProfesores(request):
    profesores = Profesor.objects.all() #trae todos los profesores creados
    contexto={"profesores":profesores}
    
    return render(request, "Aula/leerProfesores.html",contexto)


def eliminarProfesor(request, profesor_nombre):
    
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    return redirect('showProfesores')


def editProf(request, profesor_nombre):
    
    #Recibe el nombre del profesor a modificar
    prof= Profesor.objects.get(nombre=profesor_nombre)
    
    #Si es metodo POST hago lo mismo que el agregar
    if request.method=='POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid: #Si pasó la validación de Django
            info= miFormulario.cleaned_data
            prof.nombre = info['nombre']
            prof.apellido = info['apellido']
            prof.email = info['email']
            prof.profesion = info['profesion']
            
            prof.save()
        return render(request, "AppCpder/inicio.html")
    #En caso no sea post (osea GET, lo que quiere decir que es la primera ve que se entra a editar)
    else:
        miFormulario= ProfesorFormulario(initial={'nombre': prof.nombre, 
            'apellido':prof.apellido, 'email':prof.email, 'profesion': prof.profesion})
        #Voy al html que me permite editar
        return render(request,"AppCpder/editProfesor.html",{"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})
