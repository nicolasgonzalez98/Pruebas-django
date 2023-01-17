from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()

class Instructor(models.Model):
    nombre = models.CharField(max_length=128)
    email = models.CharField(max_length=50)
    cursos_asignados = models.IntegerField()
