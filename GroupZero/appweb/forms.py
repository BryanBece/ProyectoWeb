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
        fields = "nombreObra", "medidas", "tecnica", "precio", "imagenObra", "historia"