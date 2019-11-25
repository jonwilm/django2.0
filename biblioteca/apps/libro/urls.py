from django.urls import path
from .views import Libro, CrearAutor

urlpatterns = [
    path('', Libro, name = 'index_libro'),
    path('crear_autor/', CrearAutor, name = 'crear_autor')
]