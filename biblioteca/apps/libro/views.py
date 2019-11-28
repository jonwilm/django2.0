from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import FormAutor
from .models import Autor

def Libro(request):
    return render(request, 'libro/index.html')

def CrearAutor(request):
    # Comprobar Envio de Form
    if request.method == 'POST':
        # Datos de form en variable
        form_autor = FormAutor(request.POST)
        # Validar datos de form
        if form_autor.is_valid():
            # Guardar datos de form
            form_autor.save()
            # Redireccionar a url
            return redirect('libro:listar_autor')
    else:
        form_autor = FormAutor()
    return render(request, 'libro/crear_autor.html', {'form_autor': form_autor})

def ListarAutor(request):
    # Traer los autores a una variable
    autores = Autor.objects.all()
    return render(request, 'libro/listar_autor.html', {'autores': autores})

def EditarAutor(request, id):
    form_autor = None
    error = None
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            form_autor = FormAutor(instance = autor)
        else:
            form_autor = FormAutor(request.POST, instance = autor)
            if form_autor.is_valid():
                form_autor.save()
            return redirect('libro:listar_autor')
    except ObjectDoesNotExist as e:
        error = e    
    return render(request, 'libro/crear_autor.html', {'form_autor': form_autor, 'error': error})

def EliminarAutor(request, id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.delete()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html', {'autor': autor})
