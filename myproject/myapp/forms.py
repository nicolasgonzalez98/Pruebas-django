from django import forms

class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    inscriptos = forms.IntegerField(label="Inscriptos")
    solo_empresas = forms.BooleanField(label="¿Solo empresas?", required=False)
    TURNOS = (
    (1, "Mañana"),
    (2, "Tarde"),
    (3, "Noche")
    )
    turno = forms.ChoiceField(label="Turno", choices=TURNOS)
    fecha_inicio = forms.DateField(
        label="Fecha de inicio",
        widget=forms.DateInput(attrs={"type": "date"})
    )

class FormularioPelicula(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    estreno = forms.DateField(
        label="Fecha de estreno",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    mayores_de = forms.IntegerField(label='Mayores de: ')
    preventa = forms.BooleanField(label='¿Preventa online?', required=False)