from django.db import models

# Create your models here.

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