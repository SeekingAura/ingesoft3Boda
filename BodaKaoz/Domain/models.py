from django.db import models
from django.contrib.auth.models import User

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
class Decoracion(models.Model):
	nombre=models.CharField(max_length=50, null=True, blank=True, default=None)
	descripcion=models.CharField(max_length=50, null=True, blank=True, default=None)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		verbose_name = "Decoración"
		verbose_name_plural = "Decoraciones"
	
	def __str__(self):
		return self.nombre
	
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
		
#Pareja Models
		
class Enamorado(models.Model):
	User=models.OneToOneField(User, on_delete=models.CASCADE)
	cedula=models.CharField(max_length=50, validators=[numeric_validator])
	telefono=models.CharField(max_length=50, null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'Pareja'
	def __str__(self):
		return self.User.first_name+" "+self.User.last_name+"-"+self.cedula
		
class Belleza(models.Model):
	maquillaje=models.CharField(max_length=50, null=True, blank=True, default=None)
	peinado=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
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
	precio=models.IntegerField(default=0)
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
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'Pareja'
		
class PrendaCarrito(models.Model):
	Enamorado=models.ForeignKey(Enamorado, on_delete=models.CASCADE)
	Prenda=models.ForeignKey(Prenda, on_delete=models.CASCADE)
	class Meta:
		app_label = 'Pareja'
		
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
		
# Ceremonia Models

	
class Ministro(models.Model):
	nombre=models.CharField(max_length=50)
	tipo=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'Ceremonia'
		
class Musica(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'Ceremonia'
		
class CeremoniaEvento(models.Model):
	Boda=models.ForeignKey(Boda, on_delete=models.CASCADE)
	Lugar=models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Ministro=models.ForeignKey(Ministro, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Musica=models.ForeignKey(Musica, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Fotos=models.ForeignKey(Fotos, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	class Meta:
		app_label = 'Ceremonia'
	
class DecoracionCeremoniaCarrito(models.Model):
	Decoracion=models.ForeignKey(Decoracion, on_delete=models.CASCADE)
	CeremoniaEvento=models.ForeignKey(CeremoniaEvento, on_delete=models.CASCADE)
	cantidad=models.IntegerField()
	class Meta:
		app_label = 'Ceremonia'
		
# Fiesta Models

class Entretenimiento(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'Fiesta2'
		
class Alimento(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'Fiesta1'
		
class FiestaEvento(models.Model):
	Boda=models.ForeignKey(Boda, on_delete=models.CASCADE)
	Lugar=models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	Fotos=models.ForeignKey(Fotos, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'Fiesta1'
		
class EntretenimientoCarrito(models.Model):
	FiestaEvento=models.ForeignKey(CeremoniaEvento, on_delete=models.CASCADE)
	Entretenimiento=models.ForeignKey(Entretenimiento, on_delete=models.CASCADE)
	class Meta:
		app_label = 'Fiesta2'
		
class AlimentoCarrito(models.Model):
	FiestaEvento=models.ForeignKey(CeremoniaEvento, on_delete=models.CASCADE)
	Alimento=models.ForeignKey(Alimento, on_delete=models.CASCADE)
	class Meta:
		app_label = 'Fiesta1'
		
class DecoracionFiestaCarrito(models.Model):
	FiestaEvento=models.ForeignKey(CeremoniaEvento, on_delete=models.CASCADE)
	Decoracion=models.ForeignKey(Decoracion, on_delete=models.CASCADE)
	cantidad=models.IntegerField()
	class Meta:
		app_label = 'Fiesta2'
		
# LunaMiel - Models

class Plan(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	class Meta:
		app_label = 'LunaMiel'
		verbose_name = "Plan"
		verbose_name_plural = "Planes"
		
class Actividad(models.Model):
	Plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
	nombre=models.CharField(max_length=50)
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'LunaMiel'
		verbose_name = "Actividad"
		verbose_name_plural = "Actividades"
		
class Hotel(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	calificacion=models.IntegerField()
	imagen=models.ImageField(null=True, blank=True, default=None)
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'LunaMiel'
		verbose_name = "Hotel"
		verbose_name_plural = "Hoteles"
		
class ActividadPlan(models.Model):
	Plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
	Actividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
	class Meta:
		app_label = 'LunaMiel'
		verbose_name = "Actividad plan"
		verbose_name_plural = "Actividad planes"
		
class HotelPlan(models.Model):
	Plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
	Hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
	class Meta:
		app_label = 'LunaMiel'
		verbose_name = "Hotel plan"
		verbose_name_plural = "Hotel planes"
class LunaMielEvento(models.Model):
	Boda=models.ForeignKey(Boda, on_delete=models.CASCADE)
	precio=models.IntegerField(default=0)
	class Meta:
		app_label = 'LunaMiel'
		
class ActividadCarrito(models.Model):
	LunaMielEvento=models.ForeignKey(LunaMielEvento, on_delete=models.CASCADE)
	Actividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
	class Meta:
		app_label = 'LunaMiel'
		
class HotelCarrito(models.Model):
	Hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
	LunaMielEvento=models.ForeignKey(LunaMielEvento, on_delete=models.CASCADE)
	class Meta:
		app_label = 'LunaMiel'

	


	