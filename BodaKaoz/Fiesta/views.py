from django.http import HttpResponse
from django.template.loader import get_template
from Domain.models import Boda
from Domain.models import Lugar
from .models import FiestaEvento, AlimentoCarrito, Alimento, EntretenimientoCarrito, Entretenimiento


def fiestaDashboardView(request):
	boda_id = request.GET.get('boda_id')
	boda = Boda.objects.filter(id__exact=boda_id)
	fiesta = FiestaEvento.objects.get(Boda_id=boda_id)
	alimento = AlimentoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
	entretenimiento = EntretenimientoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
	indices_alimentos = []
	indices_entretenimientos = []

	count_entre = EntretenimientoCarrito.objects.all()
	count_comida = AlimentoCarrito.objects.all()	

	if len(count_entre) > 0:
		flag_entre = True
	else:
		flag_entre = False

	if len(count_comida) > 0:
		flag_comida = True
	else:
		flag_comida = False

	if fiesta.Lugar != None:
		flag_place = True
	else:
		flag_place = False

	if fiesta.Fotos:
		flag_foto = True
	else:
		flag_foto = False

	Fiesta = None
	if request.method == 'GET':
		boda_id = request.GET.get('boda_id')
		Lugares = Lugar.objects.all()
		Alimentos = Alimento.objects.all()
		Entretenimientos = Entretenimiento.objects.all()
		alimento = AlimentoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
		entretenimiento = EntretenimientoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
		
		indices_alimentos.clear()
		indices_entretenimientos.clear()

		if alimento.count() > 0:
			for a in alimento:
				indices_alimentos.append(a.Alimento.id)

		if entretenimiento.count() > 0:
			for e in entretenimiento:
				indices_entretenimientos.append(e.Entretenimiento.id)

		if len(boda_id) > 0:
			boda = Boda.objects.filter(id__exact=boda_id)

			template = get_template('Fiesta/fiesta.html')
		context = {
			'Lugares' : Lugares,
			'flag_place' : flag_place,
			'flag_foto' : flag_foto,
			'flag_entre' : flag_entre,
			'flag_comida' : flag_comida,
			'fiesta' : fiesta,
			'alimento' : alimento,
			'Alimentos' : Alimentos,
			'indices_alimentos' : indices_alimentos,
			'entretenimiento' : entretenimiento,
			'Entretenimientos' : Entretenimientos,
			'indices_entretenimientos' : indices_entretenimientos,
			'precio' : fiesta.precio
		}
		return HttpResponse(template.render(context, request))

	if request.method == 'POST':
		boda_id = request.GET.get('boda_id')
		fiesta = FiestaEvento.objects.get(Boda_id=boda_id)
		value_btn = request.POST.get('btn_value')
		Alimentos = Alimento.objects.all()
		alimento = AlimentoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
		Entretenimientos = Entretenimiento.objects.all()
		entretenimiento = EntretenimientoCarrito.objects.filter(FiestaEvento_id=fiesta.id)


		if alimento.count() > 0:
			indices_alimentos.clear()
			for a in alimento:
				indices_alimentos.append(a.Alimento.id)

		if entretenimiento.count() > 0:
			for e in entretenimiento:
				indices_entretenimientos.append(e.Entretenimiento.id)
		
		if value_btn == "add_place":
			id_place = request.POST.get('id_place')
			price = request.POST.get('price')
			fiesta.Lugar_id = id_place
			fiesta.precio = fiesta.precio + int(price)
			flag_place = True
			fiesta.save()

		if value_btn == "add_foto":
			flag_foto = True
			fiesta.Fotos=True
			fiesta.save()

		if value_btn == "add_comida":
			cantidad_comida = request.POST.get('cantidad_comida')
			flag_comida = True
			id_comida = request.POST.get('id_comida')
			price = request.POST.get('price')
			comida_inst = Alimento.objects.filter(id__exact=id_comida)
			comida = AlimentoCarrito(FiestaEvento = fiesta , Alimento = comida_inst[0], Cantidad = cantidad_comida)
			fiesta.precio = fiesta.precio + (int(price) * int (cantidad_comida))
			fiesta.save()
			comida.save()
			alimento = AlimentoCarrito.objects.filter(FiestaEvento_id=fiesta.id)

			indices_alimentos.clear()

			if alimento.count() > 0:
				for a in alimento:
					indices_alimentos.append(a.Alimento.id)

		if value_btn == "add_entretenimiento":
			flag_entre = True
			id_entre = request.POST.get('id_entretenimiento')
			price = request.POST.get('price')
			fiesta.precio = fiesta.precio + int(price)
			fiesta.save()
			entre_inst = Entretenimiento.objects.filter(id__exact=id_entre)
			entre = EntretenimientoCarrito(FiestaEvento = fiesta , Entretenimiento = entre_inst[0])
			entre.save()
			entretenimiento = EntretenimientoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
			indices_entretenimientos.clear()

			if entretenimiento.count() > 0:
				for e in entretenimiento:
					indices_entretenimientos.append(e.Entretenimiento.id)



		if value_btn == "delete_lugar":
			fiesta.Lugar = None
			price = request.POST.get('price')
			fiesta.precio = fiesta.precio - int(price)
			flag_place = False
			fiesta.save()

		if value_btn == "delete_foto":
			fiesta.Fotos=False
			flag_foto = False
			fiesta.save()
			

		if value_btn == "delete_comida":
			comida_id = request.POST.get('comida_id')
			alimento_carrito_id = request.POST.get('alimento_carrito_id')
			alimentocarrito = AlimentoCarrito.objects.filter(id__exact=alimento_carrito_id)
			cantidad = alimentocarrito[0].Cantidad
			alimentocarrito.delete()
			alimento = AlimentoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
			indices_alimentos.clear()
			price = request.POST.get('price')
			fiesta.precio = int(fiesta.precio) - (cantidad  * int(price))
			fiesta.save()
			flag_comida = False

			if alimento.count() > 0:
				for a in alimento:
					indices_alimentos.append(a.Alimento.id)

		if value_btn == "delete_entretenimiento":
			entretenimiento_id = request.POST.get('entretenimiento_id')
			entretenimiento_carrito_id = request.POST.get('entretenimiento_carrito_id')
			entre = Entretenimiento.objects.get(id=entretenimiento_id)
			entretenimientocarrito = EntretenimientoCarrito.objects.filter(id__exact=entretenimiento_carrito_id)
			entretenimientocarrito.delete()

			entretenimiento = EntretenimientoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
			indices_entretenimientos.clear()
			price = request.POST.get('price')
			fiesta.precio = int(fiesta.precio) - int(price)
			fiesta.save()
			flag_entre = False

			if entretenimiento.count() > 0:
				for e in entretenimiento:
					indices_entretenimientos.append(e.Entretenimiento.id)

			


		
		Lugares = Lugar.objects.all()
		
		template = get_template('Fiesta/fiesta.html')
		context = {
			'Lugares' : Lugares,
			'flag_place' : flag_place,
			'flag_foto' : flag_foto,
			'flag_entre' : flag_entre,
			'flag_comida' : flag_comida,
			'fiesta' : fiesta,
			'alimento' : alimento,
			'Alimentos' : Alimentos,
			'indices_alimentos' : indices_alimentos,
			'entretenimiento' : entretenimiento,
			'Entretenimientos' : Entretenimientos,
			'indices_entretenimientos' : indices_entretenimientos,
			'precio' : fiesta.precio
		}
		return HttpResponse(template.render(context, request))

