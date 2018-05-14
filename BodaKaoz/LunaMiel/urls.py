from django.urls import path
from .views import *

app_name = 'LunaMiel'
urlpatterns = [
	path('',dashboardView , name='dashboard')
]