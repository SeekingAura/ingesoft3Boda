from django.db import models
from Domain.models import *
# Create your models here.
# Fiesta Models

class FiestaEvento(models.Model):
	Boda=models.ForeignKey(Boda, on_delete=models.CASCADE)
	Lugar=models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Fotos=models.ForeignKey(Fotos, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
		
class Alimento(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
		
class AlimentoCarrito(models.Model):
	FiestaEvento=models.ForeignKey(FiestaEvento, on_delete=models.CASCADE)
	Alimento=models.ForeignKey(Alimento, on_delete=models.CASCADE)
	Cantidad = models.IntegerField(default=1)
		
class Entretenimiento(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)

class EntretenimientoCarrito(models.Model):
	FiestaEvento=models.ForeignKey(FiestaEvento, on_delete=models.CASCADE)
	Entretenimiento=models.ForeignKey(Entretenimiento, on_delete=models.CASCADE)

class DecoracionFiesta(models.Model):
	nombre=models.CharField(max_length=50, null=True, blank=True, default=None)
	descripcion=models.CharField(max_length=50, null=True, blank=True, default=None)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		verbose_name = "Decoración"
		verbose_name_plural = "Decoraciones"
	
	def __str__(self):
		return self.nombre

class DecoracionFiestaCarrito(models.Model):
	FiestaEvento=models.ForeignKey(FiestaEvento, on_delete=models.CASCADE)
	Decoracion=models.ForeignKey(DecoracionFiesta, on_delete=models.CASCADE)
	cantidad=models.IntegerField()