import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible 
class Publicacion(models.Model):
    publi = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Fecha de Publicacion')

    def __str__(self):
        return self.publi

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Usuario(models.Model):
    publicaciones = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class Hastag(models.Model):
    publicaciones = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    hastag = models.CharField(max_length=200)

    def __str__(self):
        return self.hastag