from django.shortcuts import render

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