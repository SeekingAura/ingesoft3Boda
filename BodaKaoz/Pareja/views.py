from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import get_template
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

    

    mensaje_error = (False , "")

    mensaje_succes = (False , "")

    mensaje_delete = (False , "") 
    lista_prendas=[]
    lista_bellezas=[]
    lista_accesorios=[]    
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
        PrendasMas=Prenda.objects.filter(tipo='masculino')
        PrendasFem=Prenda.objects.filter(tipo='femenino')
        PrendasMix=Prenda.objects.filter(tipo='mixto')


        Accesorios = Accesorio.objects.all()
        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL PRIMER ENAMORADO
        belleza = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        prenda = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.id)

        accesorio=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.id)   

        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL segundo ENAMORADO
        belleza2 = BellezaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        prenda2 = PrendaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        accesorio2=AccesorioCarrito.objects.filter(Enamorado_id=enamorado2.id) 

        template = loader.get_template('Pareja/pareja.html')
        belleza = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.id)
        prenda = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.id)
        accesorio=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.id) 

        lista_prendas.clear()
        lista_accesorios.clear()
        lista_bellezas.clear()  
        #Cagar listas con lo adquirido actualmente            
        if prenda.count()>0:
            for a in prenda:
               lista_prendas.append(a.Prenda.id)        
        if belleza.count()>0:
            for a in belleza:
                lista_bellezas.append(a.Belleza.id)
        if accesorio.count()>0:
            for a in accesorio:
                lista_accesorios.append(a.Accesorio.id)                           
        #enamorado1.precio=0
        #enamorado1.save()
        #print (Bellezas)
        context = {

            'enamorado' : enamorado1,
            #'enamorado2' : enamorado2,

            'belleza' : belleza,
            #'belleza2' : belleza2,

            'Bellezas' : Bellezas,

            'prenda' : prenda,
            #'prenda2' : prenda2,
            'Prendas' : Prendas,

            'accesorio' : accesorio,
            #'accesorio2' : accesorio2,

            'Accesorios' : Accesorios,
            'PrendasMas':PrendasMas,
            'PrendasFem':PrendasFem,
            'PrendasMix':PrendasMix,
            'precio' : getPriceFormat(enamorado1.precio),
            'lista_prendas': lista_prendas,
            'lista_bellezas': lista_bellezas,
            'lista_accesorios':lista_accesorios,
        }
        # print ("contexto", context)

        return HttpResponse(template.render(context, request))    
    


    if request.method == 'POST':

        user_id=request.user
        enamorado = Enamorado.objects.get(User_id=user_id)
        value_btn = request.POST.get('btn_value')
        try:
            boda=Boda.objects.get(Enamorado2=enamorado)  
            
        except :
            boda=Boda.objects.get(Enamorado1=enamorado)    

        enamorado1=boda.Enamorado1
        enamorado2=boda.Enamorado2
        #LISTADO DE PRODUCTOS
        Bellezas = Belleza.objects.all()
        Prendas = Prenda.objects.all()
        PrendasMas=Prenda.objects.filter(tipo='masculino')
        PrendasFem=Prenda.objects.filter(tipo='femenino')
        PrendasMix=Prenda.objects.filter(tipo='mixto')

        Accesorios = Accesorio.objects.all()

        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL PRIMER ENAMORADO
        belleza = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.id)
        prenda = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.id)
        accesorio=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.id)            
        
        #Cagar listas con lo adquirido actualmente            
        if prenda.count()>0:
            for a in prenda:
               lista_prendas.append(a.Prenda.id)        
        if belleza.count()>0:
            for a in belleza:
                lista_bellezas.append(a.Belleza.id)
        if accesorio.count()>0:
            for a in accesorio:
                lista_accesorios.append(a.Accesorio.id)                                
        
        #AGREGAR PRENDA
        if value_btn == "add_prenda":            
            prenda_id = request.POST.get('id_prenda')
            precio=request.POST.get('price')
            if int(prenda_id) not in lista_prendas:
                enamorado1.precio=enamorado1.precio + int(precio)             
                enamorado1.save()      
                prend=Prenda.objects.filter(id__exact=prenda_id)
                prenaux=PrendaCarrito.objects.create(Enamorado=enamorado1,Prenda=prend[0])
                prenaux.save()
                lista_prendas.clear()
                mensaje_succes = (True , "Tu prenda fue agregada correctamente")
                if prenda.count()>0:
                    for a in prenda:
                        lista_prendas.append(a.Prenda.id)                      
            else:
                mensaje_error=  (True , "Esta prenda ya fue agregada")


        #AGREGAR BELLEZA
        if value_btn == "add_belleza":
            belleza_id = request.POST.get('id_belleza')
            precio=request.POST.get('price')
            if int(belleza_id) not in lista_bellezas:
                enamorado1.precio=enamorado1.precio + int(precio)               
                enamorado1.save()        
                bell=Belleza.objects.filter(id__exact=belleza_id)
                bellaux=BellezaCarrito.objects.create(Enamorado=enamorado1,Belleza=bell[0])
                bellaux.save()   
                lista_bellezas.clear()
                mensaje_succes = (True , "Tu belleza fue agregada correctamente")
                if belleza.count()>0:
                    for a in belleza:
                        lista_bellezas.append(a.Belleza.id)                
            else:
                mensaje_error=  (True , "Esta belleza ya fue agregada")


        if value_btn == "add_accesorio":            
            accesorio_id = request.POST.get('id_accesorio')
            precio=request.POST.get('price')
            if int(accesorio_id) not in lista_accesorios:    
                enamorado1.precio=enamorado1.precio + int(precio)               
                enamorado1.save()       
                acce=Accesorio.objects.filter(id__exact=accesorio_id)
                acceaux=AccesorioCarrito.objects.create(Enamorado=enamorado1,Accesorio=acce[0])
                acceaux.save()    
                lista_accesorios.clear()        
                mensaje_succes = (True , "Tu accesorio fue agregada correctamente") 
                if accesorio.count()>0:
                    for a in accesorio:
                        lista_accesorios.append(a.Accesorio.id)                
            else:
                mensaje_error=  (True , "Este accesorio ya fue agregado") 
                    


        if value_btn == "delete_accesorio":
            accesorio_id = request.POST.get('accesorio_id')
            precio=request.POST.get('price')
            if int(accesorio_id)  in lista_accesorios:
                enamorado1.precio=enamorado1.precio - int(precio)
                enamorado1.save()
                carrito_accesorio_id = request.POST.get('carrito_accesorio_id')
                accesoriocarrito = AccesorioCarrito.objects.filter(id__exact=carrito_accesorio_id)
                accesoriocarrito.delete()
                mensaje_delete = (True , "Accesorio eliminado correctamente")
                lista_accesorios.clear()
                if accesorio.count()>0:
                    for a in accesorio:
                        lista_accesorios.append(a.Accesorio.id)                
            else:
                mensaje_error=  (True , "Este accesorio ya ha sido eliminado") 

            
        if value_btn == "delete_belleza":
            belleza_id = request.POST.get('belleza_id')
            if int(belleza_id)  in lista_bellezas:
                precio=request.POST.get('price')              
                enamorado1.precio=enamorado1.precio - int(precio)
                enamorado1.save()
                carrito_belleza_id = request.POST.get('carrito_belleza_id')
                bellezacarrito = BellezaCarrito.objects.filter(id__exact=carrito_belleza_id)
                bellezacarrito.delete()
                mensaje_delete = (True , "Belleza eliminada correctamente")
                lista_bellezas.clear()
                if belleza.count()>0:
                    for a in belleza:
                        lista_bellezas.append(a.Belleza.id)                  
            else:     
                mensaje_error=  (True , "Esta belleza ya ha sido eliminada") 

        if value_btn == "delete_prenda":
            prenda_id = request.POST.get('prenda_id')
            if int(prenda_id)  in lista_prendas:
                precio=request.POST.get('price')               
                enamorado1.precio=enamorado1.precio - int(precio)
                enamorado1.save()
                carrito_prenda_id = request.POST.get('carrito_prenda_id')
                prendacarrito = PrendaCarrito.objects.filter(id__exact=carrito_prenda_id)
                prendacarrito.delete()
                mensaje_delete = (True , "Prenda eliminada correctamente")
                lista_prendas.clear()
                if prenda.count()>0:
                    for a in prenda:
                        lista_prendas.append(a.Prenda.id)  
            else:     
                mensaje_error=  (True , "Esta prenda ya ha sido eliminada")                        

        template = get_template('Pareja/pareja.html')
        belleza = BellezaCarrito.objects.filter(Enamorado_id=enamorado1.id)
        prenda = PrendaCarrito.objects.filter(Enamorado_id=enamorado1.id)
        accesorio=AccesorioCarrito.objects.filter(Enamorado_id=enamorado1.id)
        #Cagar listas con lo adquirido actualmente  
        lista_prendas.clear()
        lista_accesorios.clear()
        lista_bellezas.clear()  

        if prenda.count()>0:
            for a in prenda:
               lista_prendas.append(a.Prenda.id)        
        if belleza.count()>0:
            for a in belleza:
                lista_bellezas.append(a.Belleza.id)
        if accesorio.count()>0:
            for a in accesorio:
                lista_accesorios.append(a.Accesorio.id) 
        context = {



            'enamorado' : enamorado1,
            #'enamorado2' : enamorado2,

            'belleza' : belleza,
            #'belleza2' : belleza2,

            'Bellezas' : Bellezas,

            'prenda' : prenda,
            #'prenda2' : prenda2,
            'Prendas' : Prendas,

            'accesorio' : accesorio,
            #'accesorio2' : accesorio2,

            'Accesorios' : Accesorios,
            'PrendasMas':PrendasMas,
            'PrendasFem':PrendasFem,
            'PrendasMix':PrendasMix,
            'precio' : getPriceFormat(enamorado1.precio),
            'mensaje_succes' : mensaje_succes,
            'lista_prendas': lista_prendas,
            'lista_bellezas': lista_bellezas,
            'lista_accesorios':lista_accesorios,
            'mensaje_delete' : mensaje_delete,
            'mensaje_error' : mensaje_error,            

        }          
        return HttpResponse(template.render(context, request))       
    
@login_required(login_url='index')
def Enamorado2(request):  

    mensaje_error = (False , "")

    mensaje_succes = (False , "")

    mensaje_delete = (False , "") 
    lista_prendas=[]
    lista_bellezas=[]
    lista_accesorios=[]    
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
        PrendasMas=Prenda.objects.filter(tipo='masculino')
        PrendasFem=Prenda.objects.filter(tipo='femenino')
        PrendasMix=Prenda.objects.filter(tipo='mixto')


        Accesorios = Accesorio.objects.all()
  

        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL segundo ENAMORADO
        belleza = BellezaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        prenda = PrendaCarrito.objects.filter(Enamorado_id=enamorado2.id)

        accesorio=AccesorioCarrito.objects.filter(Enamorado_id=enamorado2.id) 

        template = loader.get_template('Pareja/pareja.html')


        lista_prendas.clear()
        lista_accesorios.clear()
        lista_bellezas.clear()  
        #Cagar listas con lo adquirido actualmente            
        if prenda.count()>0:
            for a in prenda:
               lista_prendas.append(a.Prenda.id)        
        if belleza.count()>0:
            for a in belleza:
                lista_bellezas.append(a.Belleza.id)
        if accesorio.count()>0:
            for a in accesorio:
                lista_accesorios.append(a.Accesorio.id)                           
        #enamorado1.precio=0
        #enamorado1.save()
        #print (Bellezas)
        context = {

            'enamorado' : enamorado2,
            #'enamorado2' : enamorado2,

            'belleza' : belleza,
            #'belleza2' : belleza2,

            'Bellezas' : Bellezas,

            'prenda' : prenda,
            #'prenda2' : prenda2,
            'Prendas' : Prendas,

            'accesorio' : accesorio,
            #'accesorio2' : accesorio2,

            'Accesorios' : Accesorios,
            'PrendasMas':PrendasMas,
            'PrendasFem':PrendasFem,
            'PrendasMix':PrendasMix,
            'precio' : getPriceFormat(enamorado2.precio),
            'lista_prendas': lista_prendas,
            'lista_bellezas': lista_bellezas,
            'lista_accesorios':lista_accesorios,
        }
        # print ("contexto", context)

        return HttpResponse(template.render(context, request))    
    


    if request.method == 'POST':

        user_id=request.user
        enamorado = Enamorado.objects.get(User_id=user_id)
        value_btn = request.POST.get('btn_value')
        try:
            boda=Boda.objects.get(Enamorado2=enamorado)  
            
        except :
            boda=Boda.objects.get(Enamorado1=enamorado)    

        enamorado1=boda.Enamorado1
        enamorado2=boda.Enamorado2
        #LISTADO DE PRODUCTOS
        Bellezas = Belleza.objects.all()
        Prendas = Prenda.objects.all()
        PrendasMas=Prenda.objects.filter(tipo='masculino')
        PrendasFem=Prenda.objects.filter(tipo='femenino')
        PrendasMix=Prenda.objects.filter(tipo='mixto')

        Accesorios = Accesorio.objects.all()

        #LISTADO DE OBJETOS ALAMCENADOS EN EL CARRITO DEL SEGUNDO ENAMORADO
        belleza = BellezaCarrito.objects.filter(Enamorado_id=enamorado2.id)
        prenda = PrendaCarrito.objects.filter(Enamorado_id=enamorado2.id)
        accesorio=AccesorioCarrito.objects.filter(Enamorado_id=enamorado2.id)            
        
        #Cagar listas con lo adquirido actualmente            
        if prenda.count()>0:
            for a in prenda:
               lista_prendas.append(a.Prenda.id)        
        if belleza.count()>0:
            for a in belleza:
                lista_bellezas.append(a.Belleza.id)
        if accesorio.count()>0:
            for a in accesorio:
                lista_accesorios.append(a.Accesorio.id)                                
        
        #AGREGAR PRENDA
        if value_btn == "add_prenda":            
            prenda_id = request.POST.get('id_prenda')
            precio=request.POST.get('price')
            if int(prenda_id) not in lista_prendas:
                enamorado2.precio=enamorado2.precio + int(precio)             
                enamorado2.save()      
                prend=Prenda.objects.filter(id__exact=prenda_id)
                prenaux=PrendaCarrito.objects.create(Enamorado=enamorado2,Prenda=prend[0])
                prenaux.save()
                lista_prendas.clear()
                mensaje_succes = (True , "Tu prenda fue agregada correctamente")
                if prenda.count()>0:
                    for a in prenda:
                        lista_prendas.append(a.Prenda.id)                      
            else:
                mensaje_error=  (True , "Esta prenda ya fue agregada")


        #AGREGAR BELLEZA
        if value_btn == "add_belleza":
            belleza_id = request.POST.get('id_belleza')
            precio=request.POST.get('price')
            if int(belleza_id) not in lista_bellezas:
                enamorado2.precio=enamorado2.precio + int(precio)               
                enamorado2.save()        
                bell=Belleza.objects.filter(id__exact=belleza_id)
                bellaux=BellezaCarrito.objects.create(Enamorado=enamorado2,Belleza=bell[0])
                bellaux.save()   
                lista_bellezas.clear()
                mensaje_succes = (True , "Tu belleza fue agregada correctamente")
                if belleza.count()>0:
                    for a in belleza:
                        lista_bellezas.append(a.Belleza.id)                
            else:
                mensaje_error=  (True , "Esta belleza ya fue agregada")


        if value_btn == "add_accesorio":            
            accesorio_id = request.POST.get('id_accesorio')
            precio=request.POST.get('price')
            if int(accesorio_id) not in lista_accesorios:    
                enamorado2.precio=enamorado2.precio + int(precio)               
                enamorado2.save()       
                acce=Accesorio.objects.filter(id__exact=accesorio_id)
                acceaux=AccesorioCarrito.objects.create(Enamorado=enamorado2,Accesorio=acce[0])
                acceaux.save()    
                lista_accesorios.clear()        
                mensaje_succes = (True , "Tu accesorio fue agregada correctamente") 
                if accesorio.count()>0:
                    for a in accesorio:
                        lista_accesorios.append(a.Accesorio.id)                
            else:
                mensaje_error=  (True , "Este accesorio ya fue agregado") 
                    


        if value_btn == "delete_accesorio":
            accesorio_id = request.POST.get('accesorio_id')
            precio=request.POST.get('price')
            if int(accesorio_id)  in lista_accesorios:
                enamorado2.precio=enamorado2.precio - int(precio)
                enamorado2.save()
                carrito_accesorio_id = request.POST.get('carrito_accesorio_id')
                accesoriocarrito = AccesorioCarrito.objects.filter(id__exact=carrito_accesorio_id)
                accesoriocarrito.delete()
                mensaje_delete = (True , "Accesorio eliminado correctamente")
                lista_accesorios.clear()
                if accesorio.count()>0:
                    for a in accesorio:
                        lista_accesorios.append(a.Accesorio.id)                
            else:
                mensaje_error=  (True , "Este accesorio ya ha sido eliminado") 

            
        if value_btn == "delete_belleza":
            belleza_id = request.POST.get('belleza_id')
            if int(belleza_id)  in lista_bellezas:
                precio=request.POST.get('price')              
                enamorado2.precio=enamorado2.precio - int(precio)
                enamorado2.save()
                carrito_belleza_id = request.POST.get('carrito_belleza_id')
                bellezacarrito = BellezaCarrito.objects.filter(id__exact=carrito_belleza_id)
                bellezacarrito.delete()
                mensaje_delete = (True , "Belleza eliminada correctamente")
                lista_bellezas.clear()
                if belleza.count()>0:
                    for a in belleza:
                        lista_bellezas.append(a.Belleza.id)                  
            else:     
                mensaje_error=  (True , "Esta belleza ya ha sido eliminada") 

        if value_btn == "delete_prenda":
            prenda_id = request.POST.get('prenda_id')
            if int(prenda_id)  in lista_prendas:
                precio=request.POST.get('price')               
                enamorado2.precio=enamorado2.precio - int(precio)
                enamorado2.save()
                carrito_prenda_id = request.POST.get('carrito_prenda_id')
                prendacarrito = PrendaCarrito.objects.filter(id__exact=carrito_prenda_id)
                prendacarrito.delete()
                mensaje_delete = (True , "Prenda eliminada correctamente")
                lista_prendas.clear()
                if prenda.count()>0:
                    for a in prenda:
                        lista_prendas.append(a.Prenda.id)  
            else:     
                mensaje_error=  (True , "Esta prenda ya ha sido eliminada")                        

        template = get_template('Pareja/pareja.html')
        belleza = BellezaCarrito.objects.filter(Enamorado_id=enamorado2.id)
        prenda = PrendaCarrito.objects.filter(Enamorado_id=enamorado2.id)
        accesorio=AccesorioCarrito.objects.filter(Enamorado_id=enamorado2.id)
        lista_prendas.clear()
        lista_accesorios.clear()
        lista_bellezas.clear()  

        if prenda.count()>0:
            for a in prenda:
               lista_prendas.append(a.Prenda.id)        
        if belleza.count()>0:
            for a in belleza:
                lista_bellezas.append(a.Belleza.id)
        if accesorio.count()>0:
            for a in accesorio:
                lista_accesorios.append(a.Accesorio.id)
        context = {



            'enamorado' : enamorado2,
            #'enamorado2' : enamorado2,

            'belleza' : belleza,
            #'belleza2' : belleza2,

            'Bellezas' : Bellezas,

            'prenda' : prenda,
            #'prenda2' : prenda2,
            'Prendas' : Prendas,

            'accesorio' : accesorio,
            #'accesorio2' : accesorio2,

            'Accesorios' : Accesorios,
            'PrendasMas':PrendasMas,
            'PrendasFem':PrendasFem,
            'PrendasMix':PrendasMix,
            'precio' : getPriceFormat(enamorado2.precio),
            'mensaje_succes' : mensaje_succes,
            'lista_prendas': lista_prendas,
            'lista_bellezas': lista_bellezas,
            'lista_accesorios':lista_accesorios,
            'mensaje_delete' : mensaje_delete,
            'mensaje_error' : mensaje_error,            

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

        
        error = (False, "")
        mensaje = (False, "")
        template = loader.get_template('Pareja/registro.html') # get template
        if request.method == "GET":
           
            

            ctx = {

            'mensaje': mensaje,
            'error': error,

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
            contrasenaAut = request.POST.get("passwordAut")
            if contrasena==contrasenaAut:

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
            else:
                error=(True,"Contraseña no coincide")

            ctx = {

            'mensaje': mensaje,
            'error': error,

            }                  
            return HttpResponse(template.render(ctx, request))
