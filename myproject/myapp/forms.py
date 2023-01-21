from django import forms
from django.forms import ModelForm
from .models import Curso

class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ("nombre", "inscriptos", "turno")

class FormularioPelicula(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    estreno = forms.DateField(
        label="Fecha de estreno",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    mayores_de = forms.IntegerField(label='Mayores de: ')
    preventa = forms.BooleanField(label='¿Preventa online?', required=False)