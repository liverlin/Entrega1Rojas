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


from .forms import UserRegisterForm, UserEditForm
from .models import Avatar

from AppCpder.models import Curso
from AppCpder.forms import CursoFormulario, UserRegisterForm, UserEditForm

#@login_required #Ahora con esta linea solopodré acceder a inicio si es que estoy logueado
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
    
    return render(request, "AppCpder/inicio.html", {"mensaje":respuesta})



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
def editarPerfil(request):
    user_extension_logued, _ = Avatar.objects.get_or_create(user=request.user)
    form = UserEditForm(
        initial={
            'email' : request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'additional_description': user_extension_logued.additional_description,
        }
    )

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES)

        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            user_extension_logued.additional_description = form.cleaned_data['additional_description']

            if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()

            return render(request, 'AppCpder/inicio.html', {'mensaje': 'Usuario actualizado correctamente'})
        
        else:
            return render(request, 'AppCpder/editarPerfil.html', {'form': form, 'mensaje': 'El formulario no es valido.'})
    
    form = UserEditForm(
        initial={
            'email' : request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'additional_description': user_extension_logued.additional_description,
        }
    )

    return render(request, 'AppCpder/editarPerfil.html', {'form': form})


@login_required
def user_info(request):
    user_data, _ = Avatar.objects.get_or_create(user=request.user)
    return render(request, 'AppCpder/info_user.html', {'user_data':user_data})


def about(request):
    
    return render(request, "AppCpder/About.html")
