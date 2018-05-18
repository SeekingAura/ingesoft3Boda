var tabla_actividad_anadir = $('#tabla_actividad_anadir').DataTable({
            order:[
                [
                1,'asc'
                ]
            ]
        });

var tabla_hotel_anadir = $('#tabla_hotel_anadir').DataTable({
            order:[
                [
                1,'asc'
                ]
            ]
        });

if (typeof added == undefined){
    var added=[];
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var csrftoken = getCookie('csrftoken');

function mostrarPanelAnadir(id) {

  $.ajax(base_url+'/actividades',{
      method:'POST',
      data:{
          'id':id,
          'cantidad':1
      },
      success: function (data) {
          var fila = $('#tabla_actividad_anadir tr[data-id="a'+id+'"]');
            added['a'+id]={
                'id':id,
                'nombre':fila.attr('data-nombre'),
                'precio':fila.attr('data-precio'),
                'imagen':$('img',fila).attr('src'),
                'cantidad':1
            };
            anadirActividadCarrito(added['a'+id]);
            ocultarFila(tabla_actividad_anadir,id);
        },
      error: function (a,b,c) {
            alert("Error intente mas tarde");
        },
    });

}

function ocultarFila(tabla,id) {
    $.fn.dataTable.ext.search.push(
       function(settings, data, dataIndex) {
          return !($(tabla.row(dataIndex).node()).attr('data-id') in added);
       }
    );
    tabla.draw();
}

function anadirActividadCarrito(datos) {
    if ($('#tabla_actividades tr[data-id="a'+datos.id+'"]').length==0){
        $('#tabla_actividades > tbody:last-child').append('<tr data-id="a'+datos.id+'">' +
            '<td><img class="imagen" src="'+datos.imagen+'"></td>' +
            '<td>'+datos.nombre+'</td>' +
            '<td>'+datos.precio+'</td>' +
            '<td><input type="number" min="1" onchange="actualizarActividad('+datos.id+')" value="'+datos.cantidad+'" /></td>' +
            '<td>'+(datos.precio*datos.cantidad)+'</td>' +
            '<td><button class="btn btn-danger" ' +
            'onclick="removerCantidad('+datos.id+')" >' +
            '<i class="fa fa-ban"></i></button></td>' +
            '</tr>');
    }else{

        $('#tabla_actividades tr[data-id="a'+datos.id+'"] > td > input').val(datos.cantidad);
        $('#tabla_actividades tr[data-id="a'+datos.id+'"] > td:nth-child(5)').html(datos.cantidad*datos.precio);
    }
}

function actualizarActividad(id) {
var fila = $('#tabla_actividades tr[data-id="a'+id+'"]');
var cantidad = $('#tabla_actividades tr[data-id="a'+id+'"] > td > input').val();
  $.ajax(base_url+'/actividades',{
      method:'POST',
      data:{
          'id':id,
          'cantidad':cantidad
      },
      success: function (data) {
            added['a'+id]['cantidad']=cantidad
            anadirActividadCarrito(added['a'+id]);

        },
      error: function (a,b,c) {
            alert("Error intente mas tarde");
        },
    });

}

function removerCantidad(id) {

  $.ajax(base_url+'/actividades/'+id,{
      method:'DELETE',
      success: function (data) {
          $('#tabla_actividades tr[data-id="a'+id+'"]').remove();
            delete added['a'+id];
            ocultarFila(tabla_actividad_anadir,id);
        },
      error: function (a,b,c) {
            alert("Error intente mas tarde");
        },
    });

}

function anadirHotel(id) {

  $.ajax(base_url+'/hoteles',{
      method:'POST',
      data:{
          'id':id,
          'cantidad':1
      },
      success: function (data) {
          var fila = $('#tabla_hotel_anadir tr[data-id="h'+id+'"]');
            added['h'+id]={
                'id':id,
                'nombre':fila.attr('data-nombre'),
                'precio':fila.attr('data-precio'),
                'imagen':$('img',fila).attr('src'),
                'cantidad':1
            };
            anadirActividadCarrito(added['a'+id]);
            ocultarFila(tabla_actividad_anadir,id);
        },
      error: function (a,b,c) {
            alert("Error intente mas tarde");
        },
    });

}
