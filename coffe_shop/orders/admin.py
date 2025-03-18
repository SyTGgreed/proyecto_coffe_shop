from django.contrib import admin
from .models import Order, OrderProduct  # importamos los modelos

# Register your models here.

# para que los productos salgan en linea
# para registrar los inline se hace en la clase del modelo padre (OrderAdmin)
class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [                  # agregamos nuevo parametro y dentro la clase inline
        OrderProductInlineAdmin
    ]

admin.site.register(Order, OrderAdmin) # Registramos 
