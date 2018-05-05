from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.http import HttpResponse

from django.template import loader

from .models import *
from Domain.models import *
from Ceremonia.models import *
from Fiesta.models import *
from LunaMiel.models import *


from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='index')
def TableroResumen(request):
    user_id = request.user
    enamorado = Enamorado.objects.get(User_id=user_id)
    boda = Boda.objects.filter(Enamorado1_id=enamorado.id)

    if len(boda) == 0:
        boda = Boda.objects.filter(Enamorado2_id=enamorado.id)    

    fiesta = FiestaEvento.objects.filter(Boda_id=boda[0].id)

   
    ctx={
        'user_id': user_id,
        'boda_id':boda[0].id,
        'fiesta_id':fiesta[0].id,
    }
    template = loader.get_template('TableroResumen.html')

    return HttpResponse(template.render(ctx, request))


def Index(request):
    ctx={}
    template = loader.get_template('Pareja/index.html')

    return HttpResponse(template.render(ctx, request))
    
def Logout(request):
    if request.user is not None:

        logout(request)
    return redirect('index')

@login_required(login_url='index')
def Pareja(request):  

    template = loader.get_template('Pareja/pareja.html')
    if request.method == 'GET':

        print(request.user)
        user_id= request.user

        user = User.objects.filter(username=user_id)
        print(user)

        enamorado1 = Enamorado.objects.get(User_id=user_id)

        print(enamorado1)    

        user_id= request.user

        Bellezas = Belleza.objects.all()

        Prendas = Prenda.objects.all()

        Accesorios = Accesorio.objects.all()


        belleza = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        prenda = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        accesorio=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.id)



        

        context = {



            'enamorado' : enamorado1,

            'belleza' : belleza,

            'Bellezas' : Bellezas,

            'prenda' : prenda,

            'Prendas' : Prendas,

            'accesorio' : accesorio,

            'Accesorios' : Accesorios,

            'precio' : enamorado1.precio

        }
        # print ("contexto", context)

        return HttpResponse(template.render(context, request))    
    


    if request.method == 'POST':
        
        # print(request.user)
        user_id= request.user

        user = User.objects.filter(username=user_id)
        # print(user)

        enamorado1 = Enamorado.objects.get(User_id=user_id)

        # print(enamorado1)    

        user_id= request.user

        Bellezas = Belleza.objects.all()

        Prendas = Prenda.objects.all()

        Accesorios = Accesorio.objects.all()


        belleza = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.cedula)

        prenda = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.cedula)

        accesorio=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.cedula)
        boda_id = request.GET.get('boda_id')

        value_btn = request.POST.get('btn_value')





        if value_btn == "delete_prenda":

            prenda_id = request.POST.get('prenda_id')

            carrito_prenda_id = request.POST.get('carrito_prenda_id')

            prendacarrito = PrendaCarrito.objects.filter(id__exact=carrito_prenda_id)
            # print ("Prendaaaaaaaaaaaaaa",prendacarrito)
            prendacarrito.delete()
 
        context = {



            'enamorado' : enamorado1,

            'belleza' : belleza,

            'Bellezas' : Bellezas,

            'prenda' : prenda,

            'Prendas' : Prendas,

            'accesorio' : accesorio,

            'Accesorios' : Accesorios,

            'precio' : enamorado1.precio

        }           
        return HttpResponse(template.render(context, request))       
    
   
def Login(request):

    error = (False, "")
    user=None 

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')



        usuario = User.objects.filter(username=username)

        if len(usuario) != 0:

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                ctx = {

                        'error': error, 'user': user,

                }
                return redirect('tableroResumen')

            else:

                error = (True, "Password no valida")

        else:

            error = (True, "No existe el usuario " + username)



    template = loader.get_template('Pareja/index.html')

    ctx = {

        'error': error, 

    }

    return HttpResponse(template.render(ctx, request))
# Create your views here.



def Registro(request):

        

        if request.method == "GET":
            mensaje = (False, "")
            template = loader.get_template('Pareja/registro.html') # get template

            ctx = {

            'mensaje': mensaje,

            }                                    # Contexto o variables

            return HttpResponse(template.render(ctx, request))

        if request.method == "POST":
            #DATOS HOMMBRE
            nombre_persona1 = request.POST.get("nombreMEN")

            apellido_persona1 = request.POST.get("apellidoMEN")

            documento_persona1 = request.POST.get("identificacionMEN")

            telefono1 = request.POST.get("telefonoMEN")

            email1 = request.POST.get("emailMEN")

            #DATOS MUJER
            nombre_persona2 = request.POST.get("nombreWOMAN")

            apellido_persona2 = request.POST.get("apellidoWOMAN")

            documento_persona2 = request.POST.get("identificacionWOMAN")

            telefono2 = request.POST.get("telefonoWOMAN")

            email2 = request.POST.get("emailWOMAN")

            contrasena = request.POST.get("password")
            # print("holaaa")
            user1=User.objects.create(first_name=nombre_persona1,last_name=apellido_persona1, email=email1, username=documento_persona1)
                
            
            user1.set_password(contrasena)
            user1.save()            
            user2=User.objects.create(first_name=nombre_persona2, last_name=apellido_persona2, email=email2, username=documento_persona2)
            user2.set_password(contrasena)
            user2.save()

            #creacion enamorados
            enamorado1=Enamorado.objects.create(User=user1, cedula=documento_persona1, telefono=telefono1)
            enamorado1.save()
            enamorado2=Enamorado.objects.create(User=user2, cedula=documento_persona2, telefono=telefono2)
            enamorado2.save() 
            
            #creacion de Boda
            Boda1=Boda.objects.create(Enamorado1=enamorado1,Enamorado2=enamorado2)
            Boda1.save()
            #CREACION CEREMONIA
            CeremoniaEvento1=CeremoniaEvento.objects.create(Boda=Boda1)
            #CREACION FIESTA
            FiestaEvento1=FiestaEvento.objects.create(Boda=Boda1)
            #CREACION LUNA DE MIEL
            LunaMielEvento1=LunaMielEvento.objects.create(Boda=Boda1)
            
            mensaje = (True, "La persona fue ingresada en el sistema")

            return redirect('index')
