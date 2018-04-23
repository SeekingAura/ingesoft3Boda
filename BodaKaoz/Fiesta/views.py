from django.http import HttpResponse
from django.template.loader import get_template

def fiestaDashboardView(request):
	template = get_template('Fiesta/fiesta.html')
	context = {}
	return HttpResponse(template.render(context, request))