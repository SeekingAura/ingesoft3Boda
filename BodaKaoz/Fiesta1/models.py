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
		
