from django.db import models
from Domain.models import *
from Fiesta1.models import *

# Create your models here.
class Entretenimiento(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)

class EntretenimientoCarrito(models.Model):
	FiestaEvento=models.ForeignKey(FiestaEvento, on_delete=models.CASCADE)
	Entretenimiento=models.ForeignKey(Entretenimiento, on_delete=models.CASCADE)

class DecoracionFiestaCarrito(models.Model):
	FiestaEvento=models.ForeignKey(FiestaEvento, on_delete=models.CASCADE)
	Decoracion=models.ForeignKey(Decoracion, on_delete=models.CASCADE)
	cantidad=models.IntegerField()