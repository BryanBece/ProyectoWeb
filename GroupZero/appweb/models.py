from django.db import models
from django.contrib.auth.models import User

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
    #estado= models.TextField(Default= creado)
    #aprobado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
    
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=100)
    estilo = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto_perfil = models.ImageField(upload_to='fotos_artista/')
    Grupo = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nombre

list_estado_obra = [
    (0,'En Espera de Aprobación'),
    (1,'En Exhibición'),
    (2,'Rechazado')
]

list_categoria_obra = [
    (0,'Pintura'),
    (1,'Escultura'),
    (2,'Carpintería'),
]

#class Categoria(models)
        
class Obra(models.Model):
    nombreObra = models.CharField(max_length=50)
    nombreApellido_Autor = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    medidas = models.CharField(max_length=20)
    tecnica = models.CharField(max_length=50)
    precio = models.IntegerField()
    estado = models.IntegerField(choices=list_estado_obra, default=0)
    imagenObra = models.ImageField(upload_to='obras')
    historia = models.TextField(null=True, blank=True)
    mensaje_rechazo = models.TextField(max_length=200, null=False, blank=True)
    categoriaObra = models.IntegerField(choices=list_categoria_obra, default=0)

    def __str__(self):
        return self.nombreObra
    

class Postulacion(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    run = models.CharField(max_length=12)
    foto_perfil = models.ImageField(upload_to='fotos_perfil_postulante/')
    correo = models.EmailField()
    telefono = models.IntegerField()
    motivación = models.TextField()
    curriculum = models.FileField(upload_to='curriculums/')
    
    def __str__(self):
        return self.nombre