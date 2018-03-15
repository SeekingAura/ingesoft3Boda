from django.db import models
from Domain.models import *

# Create your models here.
# Ceremonia Models

	
class Ministro(models.Model):
	nombre=models.CharField(max_length=50)
	tipo=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
		
class Musica(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
		
class CeremoniaEvento(models.Model):
	Boda=models.ForeignKey(Boda, on_delete=models.CASCADE)
	Lugar=models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Ministro=models.ForeignKey(Ministro, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Musica=models.ForeignKey(Musica, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Fotos=models.ForeignKey(Fotos, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	
class DecoracionCeremoniaCarrito(models.Model):
	Decoracion=models.ForeignKey(Decoracion, on_delete=models.CASCADE)
	CeremoniaEvento=models.ForeignKey(CeremoniaEvento, on_delete=models.CASCADE)
	cantidad=models.IntegerField()