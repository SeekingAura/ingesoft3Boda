from django.http import HttpResponse
from django.template.loader import get_template
from Domain.models import Boda
from Domain.models import Lugar
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from Domain.models import *

# Create your views here.

def ceremoniaDashboardView(request, user_id , boda_id , ceremonia_id):
	template = get_template('Ceremonia/ceremonia.html')
	ctx={}
	return HttpResponse(template.render(ctx,request))
	
