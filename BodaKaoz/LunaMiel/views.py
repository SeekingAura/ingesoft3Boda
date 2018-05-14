from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


from .views import *
from .utils import baseContext

# Create your views here.

@login_required(login_url='index')
def dashboardView(request):
    ctx=baseContext(request)
    return render(request, 'LunaMiel/dashboard.html',ctx)