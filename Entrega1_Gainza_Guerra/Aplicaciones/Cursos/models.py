from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    puntos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.puntos)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellido)


class LenguajeProgramacion(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    puntos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.puntos)

