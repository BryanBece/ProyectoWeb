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
    #estado= models.TextField(Default= creado)
    #aprobado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
    
class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    descripcion = models.TextField()
    estilo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='artistas', null=True, blank=True)
    #user
    
    def __str__(self):
        return self.nombre

list_estado_obra = [
    (0,'Disponible'),
    (1,'Vendida'),
    (2,'En Exhibición')
]

class FormularioArt(models.Model):
    nombreObra = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    medidas = models.CharField(max_length=20)
    tecnica = models.CharField(max_length=50)
    precio = models.IntegerField()
    estado = models.IntegerField(choices=list_estado_obra)
    imagenObra = models.ImageField(upload_to='obras')
    historia = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.nombreObra

#class Categoria(models)
        
class Obra(models.Model):
    nombreObra = models.CharField(max_length=50)
    autor = models.ForeignKey(Artista, on_delete=models.PROTECT)
    medidas = models.CharField(max_length=20)
    tecnica = models.CharField(max_length=50)
    precio = models.IntegerField()
    estado = models.IntegerField(choices=list_estado_obra)
    imagenObra = models.ImageField(upload_to='obras')
    historia = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombreObra