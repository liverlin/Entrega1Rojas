from django.shortcuts import render
from models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(self):
    
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto=f"--->Curso: {curso.nombre} Camada: {curso.camada}"
    
    return HttpResponse(documentoDeTexto)