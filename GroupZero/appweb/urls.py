from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('nosotros/', nosotros, name="about"),
    path('artista/', artistas, name="artistas"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('alfredoSmith/', artista1, name="artista1"),
    path('contacto/', contacto, name="contacto"),
    path('registro_user/', registro_user, name="reg_user"),
    path('perfilArt/', login_artista, name="baseArtista"),
    path('perfilAdm/', login_administrador, name="perfilAdministrador"),
    path('galeria/', galeria, name="galeria"),
    path('registro_artista/', registro_Art, name="reg_artista"),
    path('registro_obra/', registro_obra, name="reg_obra"),
]