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

	count_deco = DecoracionCeremoniaCarrito.objects.all()


	if len(count_deco) > 0:
		flag_decoracion = True
	else:
		flag_decoracion = False

	if ceremonia.Ministro != None:
		flag_ministro = True
	else:
		flag_ministro = False

	if ceremonia.Lugar != None:
		flag_lugar = True
	else:
		flag_lugar = False

	if ceremonia.Musica != None:
		flag_musica = True
	else:
		flag_musica = False

	if ceremonia.Fotos != False:
		flag_fotos = True
	else:
		flag_fotos = False



	if request.method == 'GET':

		ministros = Ministro.objects.all()
		lugares = Lugar.objects.filter(tipo='ceremonia')
		musicas = Musica.objects.all()
		decoraciones = DecoracionCeremonia.objects.all()
		decoraciones_car = DecoracionCeremoniaCarrito.objects.all()


		if len(decoraciones_car) > 0:
			decora = []
			for decoracion in decoraciones:
				for deco in decoraciones_car:
					if decoracion.nombre != deco.Decoracion.nombre:
						decora.append(decoracion)
			decoraciones = decora



		template = get_template('Ceremonia/ceremonia.html')
		ctx={

			'ministros' : ministros,
			'flag_ministro': flag_ministro,
			'flag_fotos': flag_fotos,
			'flag_lugar': flag_lugar,
			'flag_musica': flag_musica,
			'ceremonia' : ceremonia,
			'lugares' : lugares,
			'musicas' : musicas,
			'decoraciones':decoraciones,
			'decoraciones_car':decoraciones_car,
			'flag_decoracion':flag_decoracion,

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

		if btn_value == 'add_lugar':
			price = request.POST.get('price')
			id_ministro = request.POST.get('id_lugar')
			ceremonia.Lugar_id = id_ministro
			ceremonia.precio = ceremonia.precio + int(price)
			flag_lugar = True
			ceremonia.save()

		if btn_value == 'add_musica':
			price = request.POST.get('price')
			id_musica = request.POST.get('id_musica')
			ceremonia.Musica_id = id_musica
			ceremonia.precio = ceremonia.precio + int(price)
			flag_musica = True
			ceremonia.save()

		if btn_value == 'add_fotos':
			ceremonia.Fotos = True
			flag_fotos = True
			ceremonia.save()

		if btn_value == 'delete_ministro':
			price = request.POST.get('price')
			ceremonia.Ministro_id = None
			ceremonia.precio = ceremonia.precio - int(price)
			flag_ministro = False
			ceremonia.save()

		if btn_value == 'delete_lugar':
			price = request.POST.get('price')
			ceremonia.Lugar_id = None
			ceremonia.precio = ceremonia.precio - int(price)
			flag_lugar = False
			ceremonia.save()

		if btn_value == 'delete_musica':
			price = request.POST.get('price')
			ceremonia.Musica_id = None
			ceremonia.precio = ceremonia.precio - int(price)
			flag_musica = False
			ceremonia.save()

		if btn_value == "add_decoracion":
			cantidad = request.POST.get('cantidad')
			flag_decoracion = True
			id_decoracion = request.POST.get('id_decoracion')
			price = request.POST.get('price')
			decoracion = DecoracionCeremonia.objects.filter(id__exact=id_decoracion)
			decoracion_carrito = DecoracionCeremoniaCarrito(Decoracion=decoracion[0] , CeremoniaEvento = ceremonia , cantidad = cantidad)
			ceremonia.precio = ceremonia.precio + (int(price) * int (cantidad))
			ceremonia.save()
			decoracion_carrito.save()

		if btn_value == "delete_decoracion":
			comida_id = request.POST.get('id_decoracion')
			decoracion_carrito_id = request.POST.get('id_decoracion_carrito')
			decoracioncarrito = DecoracionCeremoniaCarrito.objects.filter(id__exact=decoracion_carrito_id)
			cantidad = decoracioncarrito[0].cantidad
			decoracioncarrito.delete()
			price = request.POST.get('price')
			print(cantidad)
			print(price)
			ceremonia.precio = ceremonia.precio - (int(cantidad)  * int(price))
			ceremonia.save()

		if btn_value == 'delete_fotos':
			ceremonia.Fotos = False
			flag_fotos = False
			ceremonia.save()


		ministros = Ministro.objects.all()
		musicas = Musica.objects.all()
		lugares = Lugar.objects.filter(tipo='ceremonia')
		decoraciones = DecoracionCeremonia.objects.all()
		decoraciones_car = DecoracionCeremoniaCarrito.objects.all()

		if len(decoraciones_car) > 0:
			decora = []
			for decoracion in decoraciones:
				for deco in decoraciones_car:
					if decoracion.nombre != deco.Decoracion.nombre:
						decora.append(decoracion)
			decoraciones = decora

		template = get_template('Ceremonia/ceremonia.html')
		ctx={

			'ministros' : ministros,
			'flag_ministro': flag_ministro,
			'flag_fotos': flag_fotos,
			'flag_lugar': flag_lugar,
			'flag_musica': flag_musica,
			'flag_decoracion':flag_decoracion,
			'ceremonia' : ceremonia,
			'lugares' : lugares,
			'musicas' : musicas,
			'decoraciones':decoraciones,
			'decoraciones_car':decoraciones_car,


		}
		return HttpResponse(template.render(ctx,request))
	
