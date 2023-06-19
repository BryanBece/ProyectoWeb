from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('nosotros/', nosotros, name="about"),
    path('galeria/', galeria, name="galeria"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('alfredoSmith/', artista1, name="artista1"),
    path('contacto/', contacto, name="contacto"),
    path('registro_user/', registro_user, name="reg_user"),
]