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