from django.http import HttpResponse
from django.template.loader import get_template
from Domain.models import Boda
from Domain.models import Lugar , Fotos

def fiestaDashboardView(request):
	boda_id = request.GET.get('boda_id')

	Foto = Fotos.objects.all()
	Lugares = Lugar.objects.all()
	
	if len(boda_id) > 0:
		boda = Boda.objects.filter(id__exact=boda_id)
		print(boda[0].Enamorado1.id)
		

	template = get_template('Fiesta/fiesta.html')
	context = {}
	return HttpResponse(template.render(context, request))