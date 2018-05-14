from Domain.models import Boda
from Fiesta.models import FiestaEvento
from Pareja.models import Enamorado
from Ceremonia.models import CeremoniaEvento
from .models import LunaMielEvento
from Fiesta.utils import getPriceFormat;


def baseContext(request):

    # borrowed from pareja

    user = request.user
    enamorado = Enamorado.objects.get(User_id=user)
    boda = Boda.objects.filter(Enamorado1_id=enamorado.id)

    if len(boda) == 0:
        boda = Boda.objects.filter(Enamorado2_id=enamorado.id)

    boda = boda.first()
    fiesta = FiestaEvento.objects.filter(Boda_id=boda.id).first()
    ceremonia = CeremoniaEvento.objects.filter(Boda_id=boda.id).first()
    luna = LunaMielEvento.objects.filter(Boda_id=boda.id).first()
    precio_pareja = int(boda.Enamorado1.precio) + int(boda.Enamorado2.precio)

    return {
        'user_id': user.id,
        'boda_id':boda.id,
        'fiesta_id':fiesta.id,
        'ceremonia_id':ceremonia.id,
        'precio_fiesta': getPriceFormat(fiesta.precio),
        'precio_ceremonia': getPriceFormat(ceremonia.precio),
        'precio_luna': getPriceFormat(luna.precio),
        'precio_enamorado': getPriceFormat(boda.Enamorado1.precio),
        'precio_enamorado2': getPriceFormat(boda.Enamorado2.precio),
        'enamorado': boda.Enamorado1,
        'enamorado2': boda.Enamorado2,
        'precio_pareja': getPriceFormat(precio_pareja),
        'precio_boda': getPriceFormat(boda.precio)
    }