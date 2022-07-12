from django.db import models
from django.contrib.auth.models import User
from psutil import users

# Create your models here.

class Persona(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha = models.DateField(max_length=20)

class Publicaciones(models.Model):
    imagen = models.FileField(null=True)
    pais = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=800)
    fecha_viaje = models.DateField()      

    class Meta:
        verbose_name_plural = "Publicaciones"
        db_table = "imageupload"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='media', null=True, blank=True)