from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"  

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = "__all__"