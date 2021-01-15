from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    celular = models.CharField(max_length=9)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)


class Post(models.Model):
    #id = models.CharField(max_length=10,primary_key=True) #llave primaria
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=500)
    fecha_post = models.DateField()
    categoria = models.ManyToManyField(Categoria)

class Otro(models.Model):
    nombre = models.CharField(max_length=50)

