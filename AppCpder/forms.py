from django import forms

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
