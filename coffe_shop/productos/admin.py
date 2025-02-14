from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):  # ModelAdmin nos permite crear o registrar modelos desde el administrador
    model = Product       # le pasamos el modelo
    list_display = ['name', 'price']   # nos permite listar por los atributos del modelo producto
    search_fields = ['name']    # filtra y coloca un buscador, recibe como parametros los parametros del producto

admin.site.register(Product, ProductAdmin)