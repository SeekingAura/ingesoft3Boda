from django.contrib import admin
from .models import *
# Register your models here.
# LunaMiel
admin.site.register(Plan)
admin.site.register(Actividad)
admin.site.register(Hotel)
admin.site.register(ActividadPlan)
admin.site.register(HotelPlan)
admin.site.register(LunaMielEvento)
admin.site.register(ActividadCarrito)
admin.site.register(HotelCarrito)