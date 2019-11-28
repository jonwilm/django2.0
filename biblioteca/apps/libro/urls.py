from django.urls import path
from .views import Libro, CrearAutor, ListarAutor, EditarAutor, EliminarAutor

urlpatterns = [
    path('', Libro, name = 'index_libro'),
    path('crear_autor/', CrearAutor, name = 'crear_autor'),
    path('listar_autor/', ListarAutor, name = 'listar_autor'),
    path('editar_autor/<int:id>', EditarAutor, name = 'editar_autor'),
    path('eliminar_autor/<int:id>', EliminarAutor, name = 'eliminar_autor'),
]