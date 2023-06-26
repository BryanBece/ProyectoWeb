from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
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
    Obras = Obra.objects.all()

    #obra = Obra.objects.raw("select * from appweb_Obra where autor = user")

    data = {
        'form': ContactoForm(),
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
    publicaciones = Obra.objects.all()

    data = {
        "publicaciones": publicaciones
    }

    return render(request, 'perfilAdministrador.html', data)

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
                usu.last_name = apellido
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
                artista.contraseña = contraseña
                artista.save()

                messages.success(request, "Artista creado correctamente.")
                return redirect(reverse("home"))
    else:
        form = ArtistaForm()
    return render(request, 'registration/registroArtista.html', data)



@login_required
def registro_obra(request):

    data = {
        'form': ObraForm()
    }
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            nombreObra = form.cleaned_data.get('nombreObra')
            #nombreApellidoAutores = form.cleaned_data('nombreApellidoAutores')
            historia = form.cleaned_data.get('historia')
            imagenObra = form.cleaned_data.get('imagenObra')
            precio = form.cleaned_data.get('precio')
            tecnica = form.cleaned_data.get('tecnica')
            medidas = form.cleaned_data.get('medidas')

            obra = Obra()
            obra.nombreObra = nombreObra
            #obra.nombreApellidoAutores = nombreApellidoAutores
            obra.historia = historia
            obra.imagenObra = imagenObra
            obra.precio = precio
            obra.tecnica = tecnica
            obra.medidas = medidas
            obra.autor = request.user  # Asociar la obra con el artista actualmente conectado
            obra.save()

            messages.success(request, "Obra creada correctamente.")
            return redirect('home')
    else:
        form = ObraForm()
    return render(request, 'registration/registroObra.html', data)


def aprobarObras(request, id):
    obra = get_object_or_404(Obra, id=id)
    obra.estado = 1
    obra.save()  # Guarda la publicación actualizada en la base de datos
    messages.success(request, 'La obra: ' + obra.nombreObra + ' ha sido aprobada')

    return redirect('perfilAdministrador')

def rechazar_publicacion(request, publicacion_id):
    if request.method == 'POST':
        motivo_rechazo = request.POST.get('motivo_rechazo')
        publicacion = Obra.objects.get(id=publicacion_id)
        publicacion.estado = 2  # 2 representa el estado de "rechazado"
        publicacion.mensaje_rechazo = motivo_rechazo
        publicacion.save()
        messages.success(request, 'La publicación ha sido rechazada exitosamente.')
        return redirect('perfilAdministrador')
    else:
        messages.error(request, 'Se produjo un error al rechazar la publicación.')
        return redirect('perfilAdministrador')