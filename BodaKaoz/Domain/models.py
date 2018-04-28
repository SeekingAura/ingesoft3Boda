from django.db import models
from django.contrib.auth.models import User
from Pareja.models import *

# Validators
import re
from django.core.exceptions import ValidationError


def numeric_validator(value):
	result=re.match('[0-9]*', str(value))
	#print("el valor de value[0] es %s -" % (value[0]))
	if result is not None:	
		if len(result.group(0))!=len(str(value)):
			raise ValidationError('este campo debe ser solamente númerico')
	else:
		raise ValidationError('este campo debe ser solamente númerico')

# General Models	
class Fotos(models.Model):
	nombre=models.CharField(max_length=50, null=True, blank=True, default=None)
	descripcion=models.CharField(max_length=50, null=True, blank=True, default=None)
	tipo=models.CharField(max_length=50, null=True, blank=True, default=None)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		verbose_name = "Fotos"
		verbose_name_plural = "Fotos"
	
	def __str__(self):
		return self.nombre
	
class Lugar(models.Model):
	nombre=models.CharField(max_length=50)
	direccion=models.CharField(max_length=50)
	capacidad=models.IntegerField()
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		verbose_name = "Lugar"
		verbose_name_plural = "Lugares"
	
	def __str__(self):
		return self.nombre
		
		
# Clases de agrupamiento final
	
class Boda(models.Model):
	Enamorado1=models.ForeignKey(Enamorado, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Enamorado1')
	Enamorado2=models.ForeignKey(Enamorado, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Enamorado2')
	precio=models.IntegerField(default=0)
	
class Transporte(models.Model):
	nombre=models.CharField(max_length=50)
	tipo=models.CharField(max_length=50)
	precio=models.IntegerField(default=0)
	
class TransporteCarrito(models.Model):
	Transporte=models.ForeignKey(Transporte, on_delete=models.CASCADE)
	Boda=models.ForeignKey(Boda, on_delete=models.CASCADE)
		

		

		

	


	