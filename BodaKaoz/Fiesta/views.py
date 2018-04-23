from django.http import HttpResponse
from django.template.loader import get_template

def fiestaDashboardView(request):
	template = get_template('base/base.html')
	context = {}
	return HttpResponse(template.render(context, request))