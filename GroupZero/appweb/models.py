from django.db import models

# Create your models here.

list_tipo_contacto = [
    (0, 'Sugerencia'),
    (1, 'Reclamo'),
    (2, 'Felicitaciones'),
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=list_tipo_contacto)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    descripcion = models.TextField()
    estilo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='artistas', null=True, blank=True)
    
    def __str__(self):
        return self.nombre