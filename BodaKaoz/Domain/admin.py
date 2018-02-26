from django.contrib import admin
from .models import *


# 
admin.site.register(Boda)
admin.site.register(Transporte)
admin.site.register(TransporteCarrito)

# 
admin.site.register(Decoracion)
@admin.register(Fotos)
class FotosAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre", "tipo", "precio",)
	list_filter = ("nombre", "tipo", "precio",)
admin.site.register(Lugar)

# Pareja
admin.site.register(Enamorado)
admin.site.register(Belleza)
admin.site.register(Accesorio)
admin.site.register(Prenda)
admin.site.register(BellezaCarrito)
admin.site.register(AccesorioCarrito)
admin.site.register(PrendaCarrito)

# Ceremonia
admin.site.register(Ministro)
admin.site.register(Musica)
admin.site.register(CeremoniaEvento)
admin.site.register(DecoracionCeremoniaCarrito)

# Fiesta
admin.site.register(Entretenimiento)
admin.site.register(Alimento)
admin.site.register(FiestaEvento)
admin.site.register(EntretenimientoCarrito)
admin.site.register(AlimentoCarrito)
admin.site.register(DecoracionFiestaCarrito)

# LunaMiel
admin.site.register(Plan)
admin.site.register(Actividad)
admin.site.register(Hotel)
admin.site.register(ActividadPlan)
admin.site.register(HotelPlan)
admin.site.register(LunaMielEvento)
admin.site.register(ActividadCarrito)
admin.site.register(HotelCarrito)


