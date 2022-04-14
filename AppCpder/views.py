from django.shortcuts import render
from datetime import date
from django.http import HttpResponse
import random
from django.template import Context, Template, loader

from AppCpder.models import Curso
# Create your views here.

def inicio(request):
    return HttpResponse('Hola, soy la nueva pagina')

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo en h1<h1/>
                        ''')
    
def numero_random(request):
    numero= random.randrange(15,100)
    texto = f'Este es tu numero random{numero}'
    return HttpResponse(texto)

def numero_de_usuario(request, numero):
    texto = f'<h1> Este es tu numero de usuario: {numero} </h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    plantilla = loader.get_template('mi_plantilla_1.html')
    door=1
    dicpractica={"key":door}
    
    plantilla_preparada = plantilla.render(dicpractica)
    
    return HttpResponse(plantilla_preparada)

def probandoTemplate(self):
    nom= "Nicolas"
    ap= "Perez"
    day= date(2022,4,14)
    listaNotas= [2,2,3,7,2,5]
    
    diccionario = {
        "nombre": nom, 
        "apellido": ap,
        "fecha": day,
        "notas":listaNotas
        } #<--Para enviar el contexto
    
    plantilla =loader.get_template('plantilla_dj2.html') #Se carga en memoria nuestro documento
    #importar template y context con: from django.template import Tem,plate, Context
    #Cerramos el archivo
    #le doy el contexto mi nombre y apellido
    
    documento = plantilla.render(diccionario) #Aca renderizamos la platilla en documetnto
    
    return HttpResponse(documento)    


def curso(self):
    
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto=f"--->Curso: {curso.nombre}__Camada: {curso.camada}"
    
    return HttpResponse(documentoDeTexto)

def nuevo_curso(request):
    camada = random.randrange(1500,3000)
    nuevo_curso=Curso(nombre='Curso JS',camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}")