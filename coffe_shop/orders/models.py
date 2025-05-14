from django.db import models
from django.contrib.auth.models import User
from productos.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # si el usuario desaparece, que se borre la orden
    is_active = models.BooleanField(default=True)  # si esta activa la orden o no
    order_date = models.DateTimeField(
        auto_now_add=True
    )  # cuando se cree un campo nuevo se creara con la fecha actual

    def __str__(self):
        return f"order {self.id} by {self.user}"


class OrderProduct(models.Model):

    orden = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT
    )  # no borrar los productos que ya estan en una orden
    quantity = models.IntegerField()  # cantidad de productos que elijan

    def __str__(self):
        return f"{self.orden} - {self.product}"
