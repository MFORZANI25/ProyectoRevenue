from django.db import models

# Create your models here.
class Arquitecturas(models.Model):
    region = models.CharField(max_length=40)
    num_lista = models.IntegerField()
    num_sku= models.IntegerField()
    
    def __str__(self):
        return f"Esta arquitectura de precios pertenece a {self.region} para la lista {self.num_lista} y el artículo {self.num_sku}"
    
class Descuentos(models.Model):
    region = models.CharField(max_length=40)
    num_sku= models.IntegerField()
    
    def __str__(self):
        return f"Este descuento pertenece a {self.region} para el artículo {self.num_sku}"
    
class PrecioNeto(models.Model):
    region = models.CharField(max_length=40)
    num_lista = models.IntegerField()
    num_sku= models.IntegerField()
    
    def __str__(self):
        return f"Este es el Precio Neto de {self.region} para la lista {self.num_lista} y el artículo {self.num_sku}"
    