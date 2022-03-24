from django.db import models
from .managers import AutorManager
# Create your models here.
class Persona (models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    def __str__(self):
        return self.nombre + '-' + str(self.id)
    class Meta:
        abstract = True
class Autor(Persona):
    #CAMPOS
    
    #MANAGER
    objects = AutorManager()
    #METODOS
    