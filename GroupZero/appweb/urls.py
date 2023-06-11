from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('nosotros/', nosotros, name="about"),
    path('galeria/', galeria, name="galeria"),
    path('login/', login, name="login"),
    path('alfredoSmith/', artista1, name="artista1"),
    path('contacto/', contacto, name="contacto"),
]