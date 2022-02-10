from django.urls import path
from AppRevenue.views import arquitecturas, descuentos, precio_neto, arquitectura_formulario, descuentos_formulario, precioneto_formulario, busquedaSKU, buscar

urlpatterns = [
    path('arquitectura/', arquitecturas, name="Arquitectura"),
    path('descuento/', descuentos, name="Descuentos"),
    path('precio_neto/', precio_neto, name="Precio Neto"),
    path('arquitectura_formulario/', arquitectura_formulario, name="FormularioArquitectura"),
    path('dto_formulario/', descuentos_formulario, name="FormularioDescuento"),
    path('precioneto_formulario/', precioneto_formulario, name="FormularioPrecioNeto"),
    path('busquedaSKU/', busquedaSKU, name="BusquedaSKU"),
    path('buscar/', buscar)
]
