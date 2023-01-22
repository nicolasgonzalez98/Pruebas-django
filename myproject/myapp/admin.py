from django.contrib import admin

# Register your models here.
from .models import Curso, Profesor
admin.site.register(Curso)
admin.site.register(Profesor)