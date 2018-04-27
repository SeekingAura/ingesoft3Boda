from django.http import HttpResponse
from django.template.loader import get_template
from Domain.models import Boda
from Domain.models import Lugar , Fotos
from .models import FiestaEvento

def fiestaDashboardView(request):
	boda_id = request.GET.get('boda_id')
	boda = Boda.objects.filter(id__exact=boda_id)
	fiesta = FiestaEvento.objects.get(Boda_id=boda_id)

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
		
		if len(boda_id) > 0:
			boda = Boda.objects.filter(id__exact=boda_id)

			template = get_template('Fiesta/fiesta.html')
		context = {
			'Fotos' : Foto,
			'Lugares' : Lugares,
			'flag_place' : flag_place,
			'flag_foto' : flag_foto,
			'fiesta' : fiesta,
		}
		return HttpResponse(template.render(context, request))

	if request.method == 'POST':
		boda_id = request.GET.get('boda_id')
		fiesta = FiestaEvento.objects.get(Boda_id=boda_id)
		value_btn = request.POST.get('btn_value')
		
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

		if value_btn == "delete_lugar":
			fiesta.Lugar = None
			flag_place = False
			fiesta.save()

		if value_btn == "delete_foto":
			fiesta.Fotos = None
			flag_foto = False
			fiesta.save()

		Foto = Fotos.objects.filter(tipo__exact='fiesta')
		Lugares = Lugar.objects.all()
		
		template = get_template('Fiesta/fiesta.html')
		context = {
			'Fotos' : Foto,
			'Lugares' : Lugares,
			'flag_place' : flag_place,
			'flag_foto' : flag_foto,
			'fiesta' : fiesta,
		}
		return HttpResponse(template.render(context, request))

