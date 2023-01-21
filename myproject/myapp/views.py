from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
import requests
from . import forms
from django.urls import reverse
from .models import Curso, Instructor


# Create your views here.

api_dolar = 'https://api.recursospython.com/dollar.'

def index ( request ):
    #Ejemplo para if
    # ctx = {
    # "nombre": "Juan",
    # "cursos": 2
    # } 

    ##Ejemplo para for
    ctx = {
        "alumnos": ["Juan", "Sofía", "Matias"]
    } 

    return render(request, 'myapp/index.html', ctx)

def acerca_de ( request ):
    return HttpResponse( "¡Curso de Python y Django!" )

def cursos ( request ):
    cursos = Curso.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos.html", ctx)

def cursos_json ( request ):
    response = JsonResponse(list(Curso.objects.values()), safe=False)
    return response

def curso_name(request, nombre_curso):
    try:
        curso = Curso.objects.get(nombre=nombre_curso)
    except Curso.DoesNotExist:
        raise Http404
    ctx = {"curso": curso}
    return render(request, "myapp/curso.html", ctx)

def cotizacion_dolar(request):
    r = requests.get("https://api.recursospython.com/dollar")
    response = r.json()
    html = f"""
        <html>
        <title>Cotización del dólar</title>
        <p><strong>Compra</strong>: {response["buy_price"]}</p>
        <p><strong>Venta</strong>: {response["sale_price"]}</p>
        </html>
    """
    print(response)
    return HttpResponse(html)

def aeropuertos( request ):
    f = open('aeropuertos.csv', encoding="utf8")
    data = {'aeropuertos':[]}
    

    for linea in f:
        r = linea.split(',')
        nombre = r[1].replace('"', '')
        ciudad = r[2].replace('"', '')
        pais = r[3].replace('"', '')
        data['aeropuertos'].append({
            'nombre':r[1].replace('"', ''),
            'ciudad':r[2].replace('"', ''),
            'pais':r[3].replace('"', '')
        })
    f.close()
    
    return render(request, 'myapp/aeropuertos.html', data)

def aeropuertos_json(request):
    f = open('aeropuertos.csv', encoding="utf8")

    aeropuertos = []

    for linea in f:
        r = linea.split(',')
        dato = {
            "nombre": r[1].replace('"', ''),
            'ciudad': r[2].replace('"', ''),
            'pais' : r[3].replace('"', '')
        }
        aeropuertos.append(dato)
        
    f.close()
    return JsonResponse(aeropuertos, safe=False)

def peliculas(request, nombre_pelicula, nro_comentario):
    html = f'Comentario numero {nro_comentario} de la pelicula {nombre_pelicula}'
    return HttpResponse(html)

def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioCurso()
    ctx = {"form": form}
    return render(request, "myapp/nuevo_curso.html", ctx)

def nueva_pelicula(request):
    if request.method == "POST":
        form = forms.FormularioPelicula(request.POST)
        if form.is_valid():
            ctx = {"pelicula": form.cleaned_data}
            return render(request,'myapp/datos_pelicula.html', ctx)
    else:
        form = forms.FormularioPelicula()
    ctx = {"form": form}
    return render(request, "myapp/nueva_pelicula.html", ctx)

def instructores(request):
    datos = Instructor.objects.all()
    ctx = {"instructores": datos}
    return render(request, "myapp/instructores.html", ctx)