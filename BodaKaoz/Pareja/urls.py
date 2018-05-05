from django.urls import path
from .views import *

app_name = 'Pareja'
urlpatterns = [
	path('registrate/', Registro, name='registro'),
    #path('inicia-sesion/', Login, name='inicia-sesion'),
    path('pareja/', Pareja, name='pareja'),
    path('tablero-resumen/', TableroResumen, name='tablero-resumen'),
    #path('tablero-resumen/', TableroResumen, name='tablero-resumen'),
    path('cerrar-sesion/', Logout, name='cerrar-sesion'),
    #path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
]