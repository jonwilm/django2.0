from django.shortcuts import render, redirect
from .forms import FormAutor

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
            return redirect('index_libro')
    else:
        form_autor = FormAutor()
    return render(request, 'libro/crear_autor.html', {'form_autor': form_autor})