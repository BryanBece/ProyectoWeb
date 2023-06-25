from django import forms
from .models import *



class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"  

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = "__all__"