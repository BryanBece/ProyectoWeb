from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('nosotros/', nosotros, name="about"),
    path('galeria/', galeria, name="galeria"),
    path('login/', login, name="login"),
    path('alfredoSmith/', artista1, name="artista1"),
    path('andresCox/', artista2, name="artista2"),
    path('camilaMartinez/', artista3, name="artista3"),
    path('joseRoman/', artista4, name="artista4"),
    path('lauraHidalgo/', artista5, name="artista5"),
    path('pedroMachuca/', artista6, name="artista6"),
    path('perfilArtista/', perfilArtista, name="PerfilArtista"),
    path('perfilAdministrador/', perfilAdmin, name="PerfilAdministrador"),
]