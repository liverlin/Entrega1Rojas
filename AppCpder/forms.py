from django import forms
#Para Login/out
from django .contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    
    #Especificar los campos
    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
class ProfesorFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EstudiantesForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    
class UserRegisterForm(UserCreationForm):
    
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [ 'username','email','password1', 'password2']
        #Saca los mensajes de ayuda
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    #Defino las opciones que quiero modificar
    email= forms.EmailField(label= "Modificar E-mail")
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first = forms.CharField()
    class Meta:
        model = User
        fields = ['email','password1', 'password2', 'last_name', 'first_name']
        #Saca los mensajes de ayuda
        help_text = {k:"" for k in fields}
