from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home (request):
    return render(request, 'home.html')

def nosotros (request):
    return render(request, 'nosotros.html')

def galeria (request):
    return render(request, 'galeria.html')

def login (request):
    return render(request, 'login.html')

def artista1 (request):
    return render(request, 'alfredoSmith.html')

def artista2 (request):
    return render(request, 'andresCox.html')

def artista3 (request):
    return render(request, 'camilaMartinez.html')

def artista4 (request):
    return render(request, 'joseRoman.html')

def artista5 (request):
    return render(request, 'lauraHidalgo.html')

def artista6 (request):
    return render(request, 'pedroMachuca.html')

def perfilArtista (request):
    return render(request, 'PerfilArtista.html')

def perfilAdmin (request):
    return render(request, 'PerfilAdministrador.html')

def contacto (request):
    data = {
        'form': ContactoForm() 
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto guardado"
        else:
            data['mensaje'] = "Ha ocurrido un error"
            data["form"] = formulario

    return render(request, 'contacto.html', data)