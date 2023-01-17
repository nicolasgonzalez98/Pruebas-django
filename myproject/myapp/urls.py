from django.urls import path
from . import views

urlpatterns = [
    path( "" , views.index, name = "index" ),
    path( "acerca-de" , views.acerca_de, name = "acerca_de" ),
    path( "cursos" , views.cursos, name = "cursos" ),
    path( "cursos/json" , views.cursos_json, name = "cursos_json" ),
    path("cursos/<str:nombre_curso>", views.curso_name, name='curso_nombre'),
    path('cotizacion-dolar',views.cotizacion_dolar, name='cotizacion-dolar'),
    path('aeropuertos', views.aeropuertos, name='aeropuertos'),
    path('aeropuertos/json', views.aeropuertos_json, name='aeropuertos_json'),
    path('peliculas/<str:nombre_pelicula>/comentarios/<int:nro_comentario>', views.peliculas, name='peliculas'),
    path('nuevo-curso', views.nuevo_curso, name='nuevo-curso'),
    path('nueva-pelicula', views.nueva_pelicula, name='nueva-pelicula')
]