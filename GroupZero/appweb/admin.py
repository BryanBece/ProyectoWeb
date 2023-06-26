from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Contacto)
admin.site.register(Artista)
admin.site.register(Obra)

class AdminObra(admin.ModelAdmin):
    list_display=["nombreObra", "nombreApellidoAutores"]