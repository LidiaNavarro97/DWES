from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.http import HttpResponse, HttpResponseNotFound


BARES = [ 
    {"id": 1, "nombre": "Casa Felipe", "barrio": "La Viña", 
    "especialidad": "tortillitas de camarones", "precio": 18},

    {"id": 2, "nombre": "El Faro", "barrio": "El Pópulo", 
    "especialidad": "choco frito", "precio": 30},
    
    {"id": 3, "nombre": "Bar Cañailla", "barrio": "La Viña", 
    "especialidad": "cañailla", "precio": 22},
]


#Act 1 del punto 4 del temario:
# Respuesta: aparece 127.0.0.1 porque REMOTE_ADDR es la ip de quien hace la peticion osea el cliente
# en mi ordenador, el cliente q es el navegador y el servidor django estan en la misma maquina entonces usa la local 
def inspector(request):
    return HttpResponse(
        f"method: {request.method}\n" # get o post
        f"path:   {request.path}\n" # la ruta pedida
        f"GET:    {dict(request.GET)}\n" # los parámetros de la URL
        f"navegador: {request.headers.get('User-Agent', 'desconocido')}\n"
        f"IP cliente: {request.META.get('REMOTE_ADDR', 'desconocida')}\n" # REMOTE_ADDR es la IP del cliente
        f"Host: {request.headers.get('Host', 'desconocido')}\n", # Host es la dirección y puerto a los que se pidió la página
        content_type="text/plain; charset=utf-8"
    )


# Create yout views here.

def portada(request):
    
    return HttpResponse(
        "<h1>De tapeo por Cádiz</h1>"
        "<p>Guía de bares del casco antiguo. En obras.</p>"
    )


def listado(request):
    
    contexto = {"bares": BARES}  
    return render(request, "bares/listado.html", contexto)



def inspector(request):
    
    return HttpResponse(
            
        f"method: {request.method}\n"        
        f"path:   {request.path}\n"     
        f"GET:    {dict(request.GET)}\n",
                
        content_type="text/plain; charset=utf-8",
            
    )

# Act 2 del punto 4 del temario
def buscar(request):
    
    termino = request.GET.get("q", "").strip().casefold() # casefold pasa todo a minúsculas

    if termino == "":
        return HttpResponse("Escribe un término de búsqueda: /bares/buscar/?q=camarones")

    # escape porque el dato viene del cliente y va dentro del html
    return HttpResponse(f"Buscando «{escape(termino)}»...")  


def detalle(request, pk):
    
    for bar in BARES:
        if bar["id"] == pk:
            return render(request, "bares/detalle.html", {"bar": bar})
    
    return HttpResponseNotFound("No hay ningún bar con ese identificador.")


# Act 3 del punto 4 del temario
# Respuesta: captura solo pk, el identificador del bar q es un numero entero
# plato/ aporta solo direccion para q django sepa que ejecutar
def plato(request, pk):
    # pk llega ya como número entero porque la ruta usa <int:pk>
    return HttpResponse(f"El plato estrella del bar {pk}")    