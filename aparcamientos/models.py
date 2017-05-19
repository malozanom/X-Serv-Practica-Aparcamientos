from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Aparcamiento(models.Model):
    idEntidad = models.IntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    accesibilidad = models.IntegerField(choices=((0, '0'), (1, '1')))
    contentUrl = models.URLField(max_length=300)
    nombreVia = models.CharField(max_length=50)
    claseVial = models.CharField(max_length=50)
    tipoNum = models.CharField(max_length=10, blank=True)
    num = models.CharField(max_length=10, blank=True)
    orientacion = models.CharField(max_length=75, blank=True)
    localidad = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    codigoPostal = models.PositiveSmallIntegerField(null=True, blank=True)
    barrio = models.CharField(max_length=30)
    distrito = models.CharField(max_length=30, blank=True)
    coordenadaX = models.PositiveIntegerField()
    coordenadaY = models.PositiveIntegerField()
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    telefono = models.CharField(max_length=40, default="S/T")
    email = models.EmailField(blank=True)


class Comentario(models.Model):
    texto = models.TextField()
    aparcamiento = models.ForeignKey('Aparcamiento')


class Preferencia(models.Model):
    # Extensión del modelo de usuario: usar OneToOneField(
    # User, on_delete=models.CASCADE) o ForeignKey(User, unique=True):
    # http://stackoverflow.com/questions/31670393/difference-between-foreignkey-and-extending-the-user-class-model-in-django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, blank=True)
    tamanioLetra = models.CharField(max_length=50, blank=True)
    colorFondo = models.CharField(max_length=50, blank=True)
    # Guardar algo en blank == ""


class Seleccione(models.Model):
    aparcamiento = models.ForeignKey('Aparcamiento')
    usuario = models.ForeignKey(User)
    fechaHora = models.DateTimeField()
