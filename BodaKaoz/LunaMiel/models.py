from django.db import models
from Domain.models import *
# Create your models here.
# LunaMiel - Models


class Plan(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Planes"


class Actividad(models.Model):
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(null=True, blank=True, default=None)
    precio=models.BigIntegerField(default=0)
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"


class Hotel(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    calificacion=models.IntegerField()
    imagen=models.ImageField(null=True, blank=True, default=None)
    precio=models.BigIntegerField(default=0)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"


class ActividadPlan(models.Model):
    Plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
    Actividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    class Meta:
        verbose_name = "Actividad plan"
        verbose_name_plural = "Actividad planes"


class HotelPlan(models.Model):
    Plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
    Hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    class Meta:
        verbose_name = "Hotel plan"
        verbose_name_plural = "Hotel planes"


class LunaMielEvento(models.Model):
    Boda=models.ForeignKey(Boda, on_delete=models.CASCADE)
    precio=models.BigIntegerField(default=0)


class ActividadCarrito(models.Model):
    LunaMielEvento=models.ForeignKey(LunaMielEvento, on_delete=models.CASCADE)
    Actividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)


class HotelCarrito(models.Model):
    Hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    LunaMielEvento=models.ForeignKey(LunaMielEvento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

