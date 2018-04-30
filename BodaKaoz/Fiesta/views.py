from django.http import HttpResponse
from django.template.loader import get_template
from Domain.models import Boda
from Domain.models import Lugar , Fotos
from .models import FiestaEvento, AlimentoCarrito, Alimento, EntretenimientoCarrito, Entretenimiento


def fiestaDashboardView(request):
	boda_id = request.GET.get('boda_id')
	boda = Boda.objects.filter(id__exact=boda_id)
	fiesta = FiestaEvento.objects.get(Boda_id=boda_id)
	alimento = AlimentoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
	entretenimiento = EntretenimientoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
	indices_alimentos = []
	indices_entretenimientos = []	


	if fiesta.Lugar != None:
		flag_place = True
	else:
		flag_place = False

	if fiesta.Fotos != None:
		flag_foto = True
	else:
		flag_foto = False

	Fiesta = None
	if request.method == 'GET':
		boda_id = request.GET.get('boda_id')
		Foto = Fotos.objects.filter(tipo='fiesta')
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
			'Fotos' : Foto,
			'Lugares' : Lugares,
			'flag_place' : flag_place,
			'flag_foto' : flag_foto,
			'fiesta' : fiesta,
			'alimento' : alimento,
			'Alimentos' : Alimentos,
			'indices_alimentos' : indices_alimentos,
			'entretenimiento' : entretenimiento,
			'Entretenimientos' : Entretenimientos,
			'indices_entretenimientos' : indices_entretenimientos,
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
			fiesta.Lugar_id = id_place
			flag_place = True
			fiesta.save()

		if value_btn == "add_foto":
			id_foto = request.POST.get('id_foto')
			fiesta.Fotos_id = id_foto
			flag_foto = True
			fiesta.save()

		if value_btn == "add_comida":
			cantidad_comida = request.POST.get('cantidad_comida')
			id_comida = request.POST.get('id_comida')
			comida_inst = Alimento.objects.filter(id__exact=id_comida)
			comida = AlimentoCarrito(FiestaEvento = fiesta , Alimento = comida_inst[0], Cantidad = cantidad_comida)
			comida.save()
			alimento = AlimentoCarrito.objects.filter(FiestaEvento_id=fiesta.id)

			indices_alimentos.clear()

			if alimento.count() > 0:
				for a in alimento:
					indices_alimentos.append(a.Alimento.id)

		if value_btn == "add_entretenimiento":
			id_entre = request.POST.get('id_entretenimiento')
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
			flag_place = False
			fiesta.save()

		if value_btn == "delete_foto":
			fiesta.Fotos = None
			flag_foto = False
			fiesta.save()

		if value_btn == "delete_comida":
			comida_id = request.POST.get('comida_id')
			alimento_carrito_id = request.POST.get('alimento_carrito_id')
			alimentocarrito = AlimentoCarrito.objects.filter(id__exact=alimento_carrito_id)
			alimentocarrito.delete()
			alimento = AlimentoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
			indices_alimentos.clear()

			if alimento.count() > 0:
				for a in alimento:
					indices_alimentos.append(a.Alimento.id)

		if value_btn == "delete_entretenimiento":
			entretenimiento_id = request.POST.get('entretenimiento_id')
			entretenimiento_carrito_id = request.POST.get('entretenimiento_carrito_id')
			entretenimientocarrito = EntretenimientoCarrito.objects.filter(id__exact=entretenimiento_carrito_id)
			entretenimientocarrito.delete()
			entretenimiento = EntretenimientoCarrito.objects.filter(FiestaEvento_id=fiesta.id)
			indices_entretenimientos.clear()

			if entretenimiento.count() > 0:
				for e in entretenimiento:
					indices_entretenimientos.append(e.Entretenimiento.id)

			


		Foto = Fotos.objects.filter(tipo__exact='fiesta')
		Lugares = Lugar.objects.all()
		
		template = get_template('Fiesta/fiesta.html')
		context = {
			'Fotos' : Foto,
			'Lugares' : Lugares,
			'flag_place' : flag_place,
			'flag_foto' : flag_foto,
			'fiesta' : fiesta,
			'alimento' : alimento,
			'Alimentos' : Alimentos,
			'indices_alimentos' : indices_alimentos,
			'entretenimiento' : entretenimiento,
			'Entretenimientos' : Entretenimientos,
			'indices_entretenimientos' : indices_entretenimientos,
		}
		return HttpResponse(template.render(context, request))

