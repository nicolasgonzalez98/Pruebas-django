from django.contrib import admin

# Register your models here.
from .models import Curso, Profesor, Autor, Libro

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Autor)
admin.site.register(Libro)