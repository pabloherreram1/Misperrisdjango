from django.db import models

# Create your models here.
class Persona(models.Model):
    run = models.CharField(max_length=12)
    correo = models.CharField(max_length=100)
    nombreC = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=50)
    fecha = models.CharField(max_length=100)
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    vivienda = models.CharField(max_length=100)
    pregunta = models.CharField(max_length=30)


class Perro(models.Model):
    foto = models.ImageField(upload_to='fotos/')
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    estado = models.CharField(max_length=100)
