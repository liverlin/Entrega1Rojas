from django.shortcuts import redirect, render
#Para CRUD
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

#Para Login/out
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
#Decorador por defecto
from django.contrib.auth.decorators import login_required



from AppCpder.models import Curso, Estudiante, Profesor
from AppCpder.forms import CursoFormulario, ProfesorFormulario, EstudiantesForm, UserRegisterForm, UserEditForm

@login_required #Ahora con esta linea solopodré acceder a inicio si es que estoy logueado
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
            #return render(request,"AppCpder/inicio.html",{'profesor':new_profesor}) #Vuelvo al inicio o a donde quieran
            return render(request,"AppCpder/inicio.html") #Vuelvo al inicio o a donde quieran
    
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



def showProfesores(request):
    profesores = Profesor.objects.all() #trae todos los profesores creados
    contexto={"profesores":profesores}
    
    return render(request, "AppCpder/leerProfesores.html",contexto)


def eliminarProfesor(request, profesor_nombre):
    
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    #vuelvo al menú
    # profesores= Profesor.objects.all()
    #return render(request,"AppCpder/leerProfesores.html",{"profesores": profesores})
    #vuelvo al menú más rápido y muestro a los profesores
    return redirect('showProfesores')

# def leerProfesores(request, profesor_nombre='a'):
    
#     if profesor_nombre!='a':
#         profesor = Profesor.objects.get(nombre=profesor_nombre)
#         profesor.delete()
    
#     profesores = Profesor.objects.all() #trae todos los profesores creados
#     contexto={"profesores":profesores}
    
#     return render(request, "AppCpder/leerProfesores.html",contexto)

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

#CRUD MAS SIMPLE

class CursoList(ListView):

      model = Curso 
      template_name = "AppCpder/cursos_list.html"



class CursoDetalle(DetailView):

      model = Curso
      template_name = "AppCpder/curso_detalle.html"



class CursoCreacion(CreateView):

      model = Curso
      success_url = "/AppCpder/curso/list"
      fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

      model = Curso
      success_url = "/AppCpder/curso/list"
      fields  = ['nombre', 'camada']


class CursoDelete(DeleteView):

      model = Curso
      success_url = "/AppCpder/curso/list"


def login_request(request):
    
    if request.method =='POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user= authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request,user)
                return render(request,"AppCpder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"AppCpder/inicio.html", {"mensaje":"Error, datos incorrectos"})
        
        else:
            return render(request,"AppCpder/inicio.html", {"mensaje":"Error, fomulario errores"})
    
    form = AuthenticationForm()
    
    return render(request,"AppCpder/login.html", {"form":form})
    

def register(request):
    
    if request.method =='POST':
        
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCpder/inicio.html", {"mensaje":"Usuario creado exitosamente c:"})
        
    else:
        form = UserRegisterForm()
        
    return render(request,"AppCpder/registro.html", {"form":form})

@login_required
def editPerfil(request):
    #Instancia del login
    usuario = request.user
    
    #Si es metodo POST, hace lo mismo que el agregar
    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid: #Si pasó la validación de Django
            info= miFormulario.cleaned_data
            usuario.email= info['email']
            usuario.password1= info['password1']
            usuario.password2= info['password2']
            usuario.save()
            
        return render(request, "AppCpder/inicio.html")
    #En caso no sea post (osea GET, lo que quiere decir que es la primera ve que se entra a editar)
    else:
        #Creo el formulario con los datos que voy a modificar
        miFormulario= UserEditForm(initial={'email':info.email})
        #Voy al html que me permite editar
        return render(request,"AppCpder/editPerfil.html",{"miFormulario":miFormulario, "usuario": usuario})