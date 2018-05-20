from django.shortcuts import redirect
from django.contrib.auth import logout

def handler404View(request):
    if(request.user is not None):
        if(request.user.is_staff):
            logout(request)
    return redirect("index")