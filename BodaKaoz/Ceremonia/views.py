from django.http import HttpResponse
from django.template.loader import get_template
from Domain.models import Boda
from Domain.models import Lugar
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from Domain.models import *
from .models import *

# Create your views here.

@login_required(login_url='index')
def ceremoniaDashboardView(request, user_id , boda_id , ceremonia_id):
	
	if str(request.user) != str(user_id):
		logout(request)
		return redirect('index')

	user_id = request.user
	enamorado = Enamorado.objects.get(User_id=user_id)
	boda2 = Boda.objects.get(Enamorado1_id=enamorado.id)
	

	if str(boda2.id) != str(boda_id):
		return redirect('tableroResumen')

	boda = Boda.objects.filter(id__exact=boda_id)
	ceremonia = CeremoniaEvento.objects.get(Boda_id=boda_id)

	if str(ceremonia_id) != str(ceremonia.id):
		return redirect('tableroResumen')


	if ceremonia.Ministro != None:
		flag_ministro = True
	else:
		flag_ministro = False



	if request.method == 'GET':

		ministros = Ministro.objects.all()
		template = get_template('Ceremonia/ceremonia.html')
		ctx={

			'ministros' : ministros,
			'flag_ministro': flag_ministro,
			'ceremonia' : ceremonia,

		}
		return HttpResponse(template.render(ctx,request))

	if request.method == 'POST':
		ceremonia = CeremoniaEvento.objects.get(Boda_id=boda_id)
		btn_value = request.POST.get('btn_value')

		if btn_value == 'add_ministro':
			price = request.POST.get('price')
			id_ministro = request.POST.get('id_ministro')
			ceremonia.Ministro_id = id_ministro
			ceremonia.precio = ceremonia.precio + int(price)
			flag_ministro = True
			ceremonia.save()

		if btn_value == 'delete_ministro':
			price = request.POST.get('price')
			id_ministro = request.POST.get('id_ministro')
			ceremonia.Ministro_id = None
			ceremonia.precio = ceremonia.precio - int(price)
			flag_ministro = False
			ceremonia.save()


		ministros = Ministro.objects.all()
		template = get_template('Ceremonia/ceremonia.html')
		ctx={

			'ministros' : ministros,
			'flag_ministro': flag_ministro,
			'ceremonia' : ceremonia,

		}
		return HttpResponse(template.render(ctx,request))
	
