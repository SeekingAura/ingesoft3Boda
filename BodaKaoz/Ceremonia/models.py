from django.db import models
from Domain.models import *

# Create your models here.
# Ceremonia Models

	
class Ministro(models.Model):
	nombre=models.CharField(max_length=50)
	tipo=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.BigIntegerField(default=0)
		
class Musica(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.BigIntegerField(default=0)
		
class CeremoniaEvento(models.Model):
	Boda=models.ForeignKey(Boda, on_delete=models.CASCADE)
	Lugar=models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Ministro=models.ForeignKey(Ministro, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Musica=models.ForeignKey(Musica, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Fotos=models.BooleanField(blank=True, default=False)
	precio=models.BigIntegerField(default=0)
	

class DecoracionCeremonia(models.Model):
	nombre=models.CharField(max_length=50, null=True, blank=True, default=None)
	descripcion=models.CharField(max_length=50, null=True, blank=True, default=None)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.BigIntegerField(default=0)
	class Meta:
		verbose_name = "Decoración"
		verbose_name_plural = "Decoraciones"
	
	def __str__(self):
		return self.nombre

class DecoracionCeremoniaCarrito(models.Model):
	Decoracion=models.ForeignKey(DecoracionCeremonia, on_delete=models.CASCADE)
	CeremoniaEvento=models.ForeignKey(CeremoniaEvento, on_delete=models.CASCADE)
	cantidad=models.IntegerField()
	subtotal = models.BigIntegerField(default=0)