from django.db import models
#MIXIN Avanzado 2
#from django.contrib.auth.mixins import LoginRequiredMixin
#Para avatar
from django.contrib.auth.models import User
# Create your models here.
class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"


# class ClaseQueNecesitaLogin(LoginRequiredMixin):
    
#     def __str__(self):
#         return f"Wiii por ahora está vacía"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    link = models.URLField(null=True)
    additional_description = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"
    #Para una mejor presentacion    
    def __str__(self):
        return f"Nombre: {self.user}"