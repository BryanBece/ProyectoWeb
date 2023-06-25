from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def home(request):
    dataFormulario = {
        'form': ContactoForm
    }  
    return render(request, 'home.html', dataFormulario)

def nosotros(request):
    dataFormulario = {
        'form': ContactoForm
    }

    return render(request, 'nosotros.html', dataFormulario)

def artistas(request):
    dataFormulario = {
        'form': ContactoForm()
    }

    Artistas = Artista.objects.all()

    data = {
        'form': dataFormulario['form'],
        'Artistas': Artistas
    }

    return render(request, 'artistas.html', data)


def galeria(request):
    dataFormulario = {
        'form': ContactoForm()
    }

    Obras = Obra.objects.all()

    data = {
        'form': dataFormulario['form'],
        'Obras': Obras
    }

    return render(request, 'galeria.html', data)

# ------------------------------

def contacto(request):
    dataFormulario = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje enviado")
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        else:
            dataFormulario["form"] = formulario
            messages.error(request, "Error al enviar el mensaje")
            dataFormulario["form"] = ContactoForm()

    return render(request, 'contacto.html', dataFormulario)


def login_usuario(request):
    if request.user.groups.filter(name="Usuario"):
        return redirect("home")
    elif request.user.groups.filter(name="Artistas"):
        return redirect("baseArtista")
    elif request.user.groups.filter(name="Administrador"):
        return redirect("perfilAdministrador")
    
    messages.success(request, f"Bienvenido {request.user.username}")
    return redirect(to="home")

def login_artista(request):
    return render(request, 'perfilArtista.html')

def login_administrador(request):
    return render(request, 'perfilAdministrador.html')

def artista1(request):
    dataFormulario = {
        'form': ContactoForm
    }
    return render(request, 'artista1.html', dataFormulario)


def registro_user(request):
    dataFormulario = {
        'form': ContactoForm
    }
    
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            print("Las contraseñas no coinciden.")
        elif User.objects.filter(email=correo).exists():
            messages.error(request, "El correo ya está registrado.")
            print("El correo ya está registrado.")
        else:
            usu = User()
            usu.set_password(password1)
            usu.email = correo
            usu.username = nombre
            usu.first_name = nombre
            usu.last_name = apellido
            grupo = Group.objects.get(name="Usuario") # Cambiar a Artista si se quiere crear un artista
            
            try:
                usu.save()
                usu.groups.add(grupo)
                messages.success(request, "Usuario creado correctamente.")
                print("Usuario creado correctamente.")
                return redirect(reverse("home"))
            except:
                messages.error(request, "Error al crear el usuario.")
                print("Error al crear el usuario.")
    
    return render(request, "registration/registroUser.html", dataFormulario) # Cambiar a registroArtista.html si se quiere crear un artista



def registro_Art(request):
    data = {
        'form': ArtistaForm()
    }

    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            correo = form.cleaned_data.get('correo')
            contraseña = form.cleaned_data.get('contraseña')
            estilo = form.cleaned_data.get('estilo')
            descripcion = form.cleaned_data.get('descripcion')
            foto_perfil = form.cleaned_data.get('foto_perfil')

            if User.objects.filter(email=correo).exists():
                messages.error(request, "El correo ya está registrado.")
            else:
                usu = User()
                usu.set_password(contraseña)
                usu.email = correo
                usu.username = nombre
                usu.first_name = nombre
                usu.last_name = ""
                usu.save()

                grupo = Group.objects.get(name="Artistas")
                usu.groups.add(grupo)  # Agregar usuario al grupo "Artistas"

                artista = Artista()
                artista.nombre = nombre
                artista.apellido = apellido
                artista.correo = correo
                artista.estilo = estilo
                artista.descripcion = descripcion
                artista.foto_perfil = foto_perfil
                artista.save()

                messages.success(request, "Artista creado correctamente.")
                return redirect(reverse("home"))
    else:
        form = ArtistaForm()
    return render(request, 'registration/registroArtista.html', data)



def registroObra(request):
    if request.method == "POST":
        nombre = request.POST.get("nombreObra")
        descripcion = request.POST.get("descripcionObra")
        imagen = request.POST.get("fotoObra")
        precio = request.POST.get("precioObra")
        tecnica = request.POST.get("tecnicaObra")
        medidas = request.POST.get("medidasObra")
        
        try:
            obra = Obra()
            obra.nombreObra = nombre
            obra.historia = descripcion
            obra.imagenObra = imagen
            obra.precio = precio
            obra.tecnica = tecnica
            obra.medidas = medidas

            obra.save()
            messages.success(request, "Obra creada correctamente.")
            print("Obra creada correctamente.")
            redirect(request.META.get('HTTP_REFERER', 'home'))
        except:
            messages.error(request, "Error al crear la obra.")
            print("Error al crear la obra.")
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))