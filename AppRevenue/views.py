from django.http import HttpResponse
from django.shortcuts import render
from .models import Arquitecturas, Descuentos, PrecioNeto

# Create your views here.

def arquitecturas(request):
    return render(request, 'AppRevenue/arquitectura.html')

def descuentos(request):
    return render(request, 'AppRevenue/descuento.html')

def precio_neto(request):
    return render(request, 'AppRevenue/precio_neto.html')

def arquitectura_formulario(request):
    if request.method=='POST':
        r_region= request.POST['region']
        r_lista=request.POST['lista']
        r_sku= request.POST['sku']
        arqui= Arquitecturas(region= r_region, num_lista=r_lista, num_sku=r_sku)
        arqui.save()  
    return render(request, 'AppRevenue/arquitectura_formulario.html')

def descuentos_formulario(request):
    if request.method=='POST':
        r_region= request.POST['region']
        r_sku= request.POST['sku']
        dto= Descuentos(region= r_region, num_sku=r_sku)
        dto.save()  
    return render(request, 'AppRevenue/dto_formulario.html')

def precioneto_formulario(request):
    if request.method=='POST':
        r_region= request.POST['region']
        r_lista=request.POST['lista']
        r_sku= request.POST['sku']
        pxneto= PrecioNeto(region= r_region, num_lista=r_lista, num_sku=r_sku)
        pxneto.save()  
    return render(request, 'AppRevenue/precioneto_formulario.html')

def busquedaSKU(request):
    return render (request, 'AppRevenue/busquedaSKU.html' )

def buscar(request):
    respuesta=f"Estoy buscando el SKU: {request.GET['sku']}"
    return HttpResponse