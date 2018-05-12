from django.db import models
from Domain.models import *

# Create your models here.
# Validators
import re
from django.core.exceptions import ValidationError
TYPE=(
	('masculino','Masculino'),
	('femenino' ,'Femenino'),
	('mixto', 'Mixta')
	)

def numeric_validator(value):
	result=re.match('[0-9]*', str(value))
	#print("el valor de value[0] es %s -" % (value[0]))
	if result is not None:	
		if len(result.group(0))!=len(str(value)):
			raise ValidationError('este campo debe ser solamente númerico')
	else:
		raise ValidationError('este campo debe ser solamente númerico')

#Pareja Models
		
class Enamorado(models.Model):
	User=models.OneToOneField(User, on_delete=models.CASCADE)
	cedula=models.CharField(max_length=50, validators=[numeric_validator])
	telefono=models.CharField(max_length=50, null=True, blank=True, default=None)
	precio=models.BigIntegerField(default=0)
	class Meta:
		app_label = 'Pareja'
	def __str__(self):
		return self.User.first_name+" "+self.User.last_name+"-"+self.cedula
		
class Belleza(models.Model):
	maquillaje=models.CharField(max_length=50, null=True, blank=True, default=None)
	peinado=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.BigIntegerField(default=0)
	class Meta:
		app_label = 'Pareja'

class BellezaCarrito(models.Model):
	Enamorado=models.ForeignKey(Enamorado, on_delete=models.CASCADE)
	Belleza=models.ForeignKey(Belleza, on_delete=models.CASCADE)
	class Meta:
		app_label = 'Pareja'
		
class Accesorio(models.Model):
	nombre=models.CharField(max_length=50)
	tipoObjeto=models.CharField(max_length=50)
	alquilado=models.BooleanField(default=False)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.BigIntegerField(default=0)
	class Meta:
		app_label = 'Pareja'
		
class AccesorioCarrito(models.Model):
	Enamorado=models.ForeignKey(Enamorado, on_delete=models.CASCADE)
	Accesorio=models.ForeignKey(Accesorio, on_delete=models.CASCADE)
	class Meta:
		app_label = 'Pareja'
		
class Prenda(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	talla=models.CharField(max_length=10)
	imagen=models.ImageField(null=True, blank=True, default=None)
	tipo = models.CharField(choices=TYPE, blank=True , default=None, max_length=50)
	precio=models.BigIntegerField(default=0)
	class Meta:
		app_label = 'Pareja'
		
class PrendaCarrito(models.Model):
	Enamorado=models.ForeignKey(Enamorado, on_delete=models.CASCADE)
	Prenda=models.ForeignKey(Prenda, on_delete=models.CASCADE)
	class Meta:
		app_label = 'Pareja'
