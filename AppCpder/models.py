from django.db import models
#MIXIN Avanzado 2
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.
class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"

class Estudiante(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    
    def __str__(self):
        return f"Estudiante: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Profesor(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)

    def __str__(self):
        return f"Prof.: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion}"


# class ClaseQueNecesitaLogin(LoginRequiredMixin):
    
#     def __str__(self):
#         return f"Wiii por ahora está vacía"
