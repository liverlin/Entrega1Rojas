from django import forms
#Para Login/out
from django .contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    
    #Especificar los campos
    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
    
class UserRegisterForm(UserCreationForm):
    
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [ 'username','email','password1', 'password2']
        #Saca los mensajes de ayuda
        help_text = {k:"" for k in fields}

class UserEditForm(forms.Form):

    email = forms.EmailField(label='Modificar E-mail')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir el password', widget=forms.PasswordInput())
    last_name = forms.CharField(label="Apellido", max_length = 20)
    first_name = forms.CharField(label="Nombre", max_length = 20)
    avatar = forms.ImageField(required=False)
    link = forms.URLField(required = False)
    additional_description = forms.CharField(max_length = 100, required = False)