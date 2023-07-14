from django import forms
from .models import *



class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"  

class ArtistaForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Artista
        fields = "nombre", "apellido", "correo", "contraseña", "estilo", "descripcion", "foto_perfil"

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = "nombreObra", "nombreApellido_Autor", "medidas", "tecnica", "precio", "categoriaObra", "imagenObra", "historia"

class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postulacion
        fields = "__all__"
        labels = {
            "motivación": "Cuéntanos por qué quieres ser parte de nuestro grupo de artistas:",
        }
    