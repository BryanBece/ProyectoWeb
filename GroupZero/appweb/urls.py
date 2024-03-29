from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('nosotros/', nosotros, name="about"),
    path('artista/', artistas, name="artistas"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('contacto/', contacto, name="contacto"),
    path('registro_user/', registro_user, name="reg_user"),
    path('perfilArt/', login_artista, name="perfilArt"),
    path('perfilAdm/', login_administrador, name="perfilAdministrador"),
    path('galeria/', galeria, name="galeria"),
    path('registro_artista/', registro_Art, name="reg_artista"),
    path('registro_obra/', registro_obra, name="reg_obra"),
    path('aprobarObras/<int:id>/', views.aprobarObras, name='aprobacionObras'),
    path('rechazar-publicacion/<int:publicacion_id>/', views.rechazar_publicacion, name='rechazar_publicacion'),
    path('postulacion/', postulacion, name="postulacion"),
    path('postulaciones/', postulaciones, name="postulaciones"),
]