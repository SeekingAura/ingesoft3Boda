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


def getPriceFormat(value):

    string = str(value)

    keys = [ string[::-1][i:i+3] for i in range(0, len(string), 3)]

    finalValue = '.'.join(keys)[::-1]

    return finalValue

@login_required(login_url='index')
def TableroResumen(request):

    ctx={}
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
def Enamorado1(request):  

    template = loader.get_template('Pareja/pareja.html')

    mensaje_error = (False , "")

    mensaje_succes = (False , "")

    mensaje_delete = (False , "")     
    if request.method == 'GET':

        user_id=request.user
        enamorado = Enamorado.objects.get(User_id=user_id)

        try:
            boda=Boda.objects.get(Enamorado2=enamorado)  
            
        except :
            boda=Boda.objects.get(Enamorado1=enamorado)    

        enamorado1=boda.Enamorado1
        enamorado2=boda.Enamorado2
        print (enamorado1)
        print (enamorado2)
        print (boda.id)
        print("jajaja",enamorado1.precio)
        #LISTADO DE PRODUCTOS
        Bellezas = Belleza.objects.all()

        Prendas = Prenda.objects.all()

        Accesorios = Accesorio.objects.all()
        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL PRIMER ENAMORADO
        belleza1 = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        prenda1 = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        accesorio1=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.id)   

        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL segundo ENAMORADO
        belleza2 = BellezaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        prenda2 = PrendaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        accesorio2=AccesorioCarrito.objects.filter(Enamorado_id=enamorado2.id)                
        #enamorado1.precio=0
        #enamorado1.save()
        #print (Bellezas)
        context = {




            'enamorado' : enamorado1,
            #'enamorado2' : enamorado2,

            'belleza' : belleza1,
            #'belleza2' : belleza2,

            'Bellezas' : Bellezas,

            'prenda' : prenda1,
            #'prenda2' : prenda2,
            'Prendas' : Prendas,

            'accesorio' : accesorio1,
            #'accesorio2' : accesorio2,

            'Accesorios' : Accesorios,

            'precio' : getPriceFormat(enamorado1.precio),

        }
        # print ("contexto", context)

        return HttpResponse(template.render(context, request))    
    


    if request.method == 'POST':

        user_id=request.user
        enamorado = Enamorado.objects.get(User_id=user_id)

        try:
            boda=Boda.objects.get(Enamorado2=enamorado)  
            
        except :
            boda=Boda.objects.get(Enamorado1=enamorado)    

        enamorado1=boda.Enamorado1
        enamorado2=boda.Enamorado2
        print (enamorado1)
        print (enamorado2)
        print (boda.id)
        #LISTADO DE PRODUCTOS
        Bellezas = Belleza.objects.all()

        Prendas = Prenda.objects.all()

        Accesorios = Accesorio.objects.all()
        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL PRIMER ENAMORADO
        belleza1 = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        prenda1 = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        accesorio1=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.id)   

        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL segundo ENAMORADO
        belleza2 = BellezaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        prenda2 = PrendaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        accesorio2=AccesorioCarrito.objects.filter(Enamorado_id=enamorado2.id)         
        value_btn = request.POST.get('btn_value')



        if value_btn == "add_prenda":
            

            prenda_id = request.POST.get('id_prenda')
            precio=request.POST.get('price')
    
            enamorado1.precio=enamorado1.precio + int(precio)
            
            enamorado1.save()
    
            prend=Prenda.objects.filter(id__exact=prenda_id)
            prenaux=PrendaCarrito.objects.create(Enamorado=enamorado1,Prenda=prend[0])
            prenaux.save()
            mensaje_succes = (True , "Tu prenda fue agregada correctamente")

        if value_btn == "add_belleza":
            

            belleza_id = request.POST.get('id_belleza')
            precio=request.POST.get('price')
    
            enamorado1.precio=enamorado1.precio + int(precio)
            
            enamorado1.save()
    
            bell=Belleza.objects.filter(id__exact=belleza_id)
            bellaux=BellezaCarrito.objects.create(Enamorado=enamorado1,Belleza=bell[0])
            bellaux.save()   
            mensaje_succes = (True , "Tu belleza fue agregada correctamente")



        if value_btn == "add_accesorio":
            

            accesorio_id = request.POST.get('id_accesorio')
            precio=request.POST.get('price')
    
            enamorado1.precio=enamorado1.precio + int(precio)
            
            enamorado1.save()
    
            acce=Accesorio.objects.filter(id__exact=accesorio_id)
            acceaux=AccesorioCarrito.objects.create(Enamorado=enamorado1,Accesorio=acce[0])
            acceaux.save()            
            mensaje_succes = (True , "Tu accesorio fue agregada correctamente") 



        if value_btn == "delete_accesorio":

            accesorio_id = request.POST.get('accesorio_id')
            precio=request.POST.get('price')
            
            enamorado1.precio=enamorado1.precio - int(precio)
            enamorado1.save()
            carrito_accesorio_id = request.POST.get('carrito_accesorio_id')

            accesoriocarrito = AccesorioCarrito.objects.filter(id__exact=carrito_accesorio_id)
            # print ("Prendaaaaaaaaaaaaaa",prendacarrito)
            accesoriocarrito.delete()
            mensaje_delete = (True , "Accesorio eliminado correctamente")

            
        if value_btn == "delete_belleza":

            belleza_id = request.POST.get('belleza_id')
            precio=request.POST.get('price')
            
            enamorado1.precio=enamorado1.precio - int(precio)
            enamorado1.save()
            carrito_belleza_id = request.POST.get('carrito_belleza_id')

            bellezacarrito = BellezaCarrito.objects.filter(id__exact=carrito_belleza_id)
            # print ("Prendaaaaaaaaaaaaaa",prendacarrito)
            bellezacarrito.delete()
            mensaje_delete = (True , "Belleza eliminada correctamente")


        if value_btn == "delete_prenda":

            prenda_id = request.POST.get('prenda_id')
            precio=request.POST.get('price')
            
            enamorado1.precio=enamorado1.precio - int(precio)
            enamorado1.save()
            carrito_prenda_id = request.POST.get('carrito_prenda_id')

            prendacarrito = PrendaCarrito.objects.filter(id__exact=carrito_prenda_id)
            # print ("Prendaaaaaaaaaaaaaa",prendacarrito)
            prendacarrito.delete()
            mensaje_delete = (True , "Prenda eliminada correctamente")

 
        context = {



            'enamorado' : enamorado1,
            #'enamorado2' : enamorado2,

            'belleza' : belleza1,
            #'belleza2' : belleza2,

            'Bellezas' : Bellezas,

            'prenda' : prenda1,
            #'prenda2' : prenda2,
            'Prendas' : Prendas,

            'accesorio' : accesorio1,
            #'accesorio2' : accesorio2,

            'Accesorios' : Accesorios,

            'precio' : getPriceFormat(enamorado1.precio),
            'mensaje_succes' : mensaje_succes,

            'mensaje_delete' : mensaje_delete,            

        }          
        return HttpResponse(template.render(context, request))       
    
@login_required(login_url='index')
def Enamorado2(request):  

    template = loader.get_template('Pareja/pareja.html')

    mensaje_error = (False , "")

    mensaje_succes = (False , "")

    mensaje_delete = (False , "")    
    if request.method == 'GET':

        user_id=request.user
        enamorado = Enamorado.objects.get(User_id=user_id)

        try:
            boda=Boda.objects.get(Enamorado2=enamorado)  
            
        except :
            boda=Boda.objects.get(Enamorado1=enamorado)    

        enamorado1=boda.Enamorado1
        enamorado2=boda.Enamorado2

        #LISTADO DE PRODUCTOS
        Bellezas = Belleza.objects.all()

        Prendas = Prenda.objects.all()

        Accesorios = Accesorio.objects.all()
        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL PRIMER ENAMORADO
        belleza1 = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        prenda1 = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        accesorio1=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.id)   

        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL segundo ENAMORADO
        belleza2 = BellezaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        prenda2 = PrendaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        accesorio2=AccesorioCarrito.objects.filter(Enamorado_id=enamorado2.id)                
        #enamorado2.precio=0
        #enamorado2.save()
        #print (Bellezas)
        context = {




            'enamorado' : enamorado2,
            #'enamorado2' : enamorado2,

            'belleza' : belleza2,
            #'belleza2' : belleza2,

            'Bellezas' : Bellezas,

            'prenda' : prenda2,
            #'prenda2' : prenda2,
            'Prendas' : Prendas,

            'accesorio' : accesorio2,
            #'accesorio2' : accesorio2,

            'Accesorios' : Accesorios,

            'precio' : getPriceFormat(enamorado2.precio),

        }
        # print ("contexto", context)

        return HttpResponse(template.render(context, request))    
    


    if request.method == 'POST':

        user_id=request.user
        enamorado = Enamorado.objects.get(User_id=user_id)

        try:
            boda=Boda.objects.get(Enamorado2=enamorado)  
            
        except :
            boda=Boda.objects.get(Enamorado1=enamorado)    

        enamorado1=boda.Enamorado1
        enamorado2=boda.Enamorado2
        print (enamorado1)
        print (enamorado2)
        print (boda.id)
        #LISTADO DE PRODUCTOS
        Bellezas = Belleza.objects.all()

        Prendas = Prenda.objects.all()

        Accesorios = Accesorio.objects.all()
        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL PRIMER ENAMORADO
        belleza1 = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        prenda1 = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        accesorio1=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.id)   

        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL segundo ENAMORADO
        belleza2 = BellezaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        prenda2 = PrendaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        accesorio2=AccesorioCarrito.objects.filter(Enamorado_id=enamorado2.id)         
        value_btn = request.POST.get('btn_value')



        if value_btn == "add_prenda":
            

            prenda_id = request.POST.get('id_prenda')
            precio=request.POST.get('price')
    
            enamorado2.precio=enamorado2.precio + int(precio)
            
            enamorado2.save()
    
            prend=Prenda.objects.filter(id__exact=prenda_id)
            prenaux=PrendaCarrito.objects.create(Enamorado=enamorado2,Prenda=prend[0])
            prenaux.save()
            mensaje_succes = (True , "Tu prenda fue agregada correctamente")


        if value_btn == "add_belleza":
            

            belleza_id = request.POST.get('id_belleza')
            precio=request.POST.get('price')
    
            enamorado2.precio=enamorado2.precio + int(precio)
            
            enamorado2.save()
    
            bell=Belleza.objects.filter(id__exact=belleza_id)
            bellaux=BellezaCarrito.objects.create(Enamorado=enamorado2,Belleza=bell[0])
            bellaux.save()   
            mensaje_succes = (True , "Tu belleza fue agregada correctamente")



        if value_btn == "add_accesorio":
            

            accesorio_id = request.POST.get('id_accesorio')
            precio=request.POST.get('price')
    
            enamorado2.precio=enamorado2.precio + int(precio)
            
            enamorado2.save()
    
            acce=Accesorio.objects.filter(id__exact=accesorio_id)
            acceaux=AccesorioCarrito.objects.create(Enamorado=enamorado2,Accesorio=acce[0])
            acceaux.save()   
            mensaje_succes = (True , "Tu accesorio fue agregada correctamente")         



        if value_btn == "delete_accesorio":

            accesorio_id = request.POST.get('accesorio_id')
            precio=request.POST.get('price')
            
            enamorado2.precio=enamorado2.precio - int(precio)
            enamorado2.save()
            carrito_accesorio_id = request.POST.get('carrito_accesorio_id')

            accesoriocarrito = AccesorioCarrito.objects.filter(id__exact=carrito_accesorio_id)
            # print ("Prendaaaaaaaaaaaaaa",prendacarrito)
            accesoriocarrito.delete()
            mensaje_delete = (True , "Accesorio eliminado correctamente")

            
        if value_btn == "delete_belleza":

            belleza_id = request.POST.get('belleza_id')
            precio=request.POST.get('price')
            
            enamorado2.precio=enamorado2.precio - int(precio)
            enamorado2.save()
            carrito_belleza_id = request.POST.get('carrito_belleza_id')

            bellezacarrito = BellezaCarrito.objects.filter(id__exact=carrito_belleza_id)
            # print ("Prendaaaaaaaaaaaaaa",prendacarrito)
            bellezacarrito.delete()
            mensaje_delete = (True , "Belleza eliminada correctamente")

        if value_btn == "delete_prenda":

            prenda_id = request.POST.get('prenda_id')
            precio=request.POST.get('price')
            
            enamorado2.precio=enamorado2.precio - int(precio)
            enamorado2.save()
            carrito_prenda_id = request.POST.get('carrito_prenda_id')

            prendacarrito = PrendaCarrito.objects.filter(id__exact=carrito_prenda_id)
            # print ("Prendaaaaaaaaaaaaaa",prendacarrito)
            prendacarrito.delete()
            mensaje_delete = (True , "Prenda eliminada correctamente")
 
        context = {



            'enamorado' : enamorado2,
            #'enamorado2' : enamorado2,

            'belleza' : belleza2,
            #'belleza2' : belleza2,

            'Bellezas' : Bellezas,

            'prenda' : prenda2,
            #'prenda2' : prenda2,
            'Prendas' : Prendas,

            'accesorio' : accesorio2,
            #'accesorio2' : accesorio2,

            'Accesorios' : Accesorios,

            'precio' : getPriceFormat(enamorado2.precio),
            
            'mensaje_succes' : mensaje_succes,

            'mensaje_delete' : mensaje_delete,
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
