from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sqlite3
import requests

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
    conn = sqlite3.connect( "cursos.db" )
    cursor = conn.cursor()
    cursor.execute( "SELECT nombre, inscriptos FROM cursos" )
    html = """
        <html>
        <title>Lista de cursos</title>
        <table style="border: 1px solid">
        <thead>
        <tr>
        <th>Curso</th>
        <th>Inscriptos</th>
        </tr>
        </thead>
    """
    for (nombre, inscriptos) in cursor.fetchall():
        html += f"""
        <tr>
        <td> { nombre } </td>
        <td> { inscriptos } </td>
        </tr>
        """
        html += "</table></html>"
    conn.close()
    return HttpResponse(html)

def cursos_json ( request ):
    conn = sqlite3.connect( "cursos.db" )
    cursor = conn.cursor()
    cursor.execute( "SELECT nombre, inscriptos FROM cursos" )
    response = JsonResponse(cursor.fetchall(), safe = False )
    conn.close()
    return response

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

    html = """
        <html>
        <title>Lista de aeropuertos</title>
        <table style="border: 1px solid">
          <thead>
            <tr>
              <th>Aeropuerto</th>
              <th>Ciudad</th>
              <th>País</th>
            </tr>
          </thead>
    """

    for linea in f:
        r = linea.split(',')
        nombre = r[1].replace('"', '')
        ciudad = r[2].replace('"', '')
        pais = r[3].replace('"', '')
        html += f'''
            <tr>
                <td>{nombre}</td>
                <td>{ciudad}</td>
                <td>{pais}</td>
            </tr>
        '''
    f.close()
    html += "</table></html>"
    return HttpResponse(html)

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