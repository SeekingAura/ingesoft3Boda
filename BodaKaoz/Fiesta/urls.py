from django.urls import path
from .views import fiestaDashboardView

app_name = 'Fiesta'
urlpatterns = [
	path('', fiestaDashboardView , name='dashboard')
]