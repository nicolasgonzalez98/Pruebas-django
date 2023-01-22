from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)

    def __str__(self):
        return self.apellido+', '+self.nombre


    class Meta:
        verbose_name_plural = "Autores"

class Libro(models.Model):
    titulo = models.CharField(max_length=128)
    editorial = models.CharField(max_length=128)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.titulo} ({self.autor.apellido})'


    class Meta:
        verbose_name_plural = "Libros"

class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    monotributista = models.BooleanField()

    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name_plural = "Profesores"

class Curso(models.Model):
    nombre = models.CharField('Nombre',max_length=128)
    inscriptos = models.IntegerField("Inscriptos")
    TURNOS = (
    (1, "Mañana"),
    (2, "Tarde"),
    (3, "Noche")
    )
    turno = models.PositiveSmallIntegerField("Turno", choices=TURNOS, null=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name="cursos")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Cursos'

    

class Instructor(models.Model):
    nombre = models.CharField(max_length=128)
    email = models.CharField(max_length=50)
    cursos_asignados = models.IntegerField()
    


