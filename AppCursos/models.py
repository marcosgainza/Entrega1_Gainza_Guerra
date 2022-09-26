from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Camada:{self.codigo}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido} - Email:{self.email}"

class LenguajeProgramacion(models.Model):
   tipo = models.CharField(max_length=40)
   codigo = models.IntegerField()

   def __str__(self):
       return f"Nombre:{self.tipo} - Camada:{self.codigo}"
