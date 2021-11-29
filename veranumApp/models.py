from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # el modelo abstracto ya tiene un campo username que es correo
    #y en otro caso que tiene un campo password que es contraseña
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    pais = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    rut = models.CharField(max_length=10, null=True, blank=True)

class Habitacion(models.Model):
    id_habitacion = models.CharField(max_length=40, primary_key=True)
    tipo_Habitacion = models.CharField(max_length=50)
    cantidad_camas = models.IntegerField()
    precio = models.IntegerField()
    piso = models.IntegerField()
    estado = models.BooleanField()
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_termino = models.DateField(blank=True, null=True)
    cantidad_personas = models.IntegerField(blank=True, null=True)