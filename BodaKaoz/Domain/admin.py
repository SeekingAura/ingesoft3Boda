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










