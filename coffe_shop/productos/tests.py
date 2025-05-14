from django.test import TestCase
from django.urls import reverse

from .models import Product

# Create your tests here.


class ListProductsViewsTests(TestCase):

    def test_show_return_200(self):
        url = reverse("list_product")  # --> nombre de la url
        response = self.client.get(
            url
        )  # --> el metodo self.client permite crear un cliente http con el
        # --> que podemos hacer peticiones get, post y demas
        # breakpoint()   # --> detener la ejecucion del programa para validar las variables, nos abre una shell
        #  que permite escribir codigo python
        self.assertEqual(response.status_code, 200)  # -> .equals compara si son iguales
        self.assertEqual(
            response.context["products"].count(), 0
        )  # -> comparamos si el contador de productos es = 0

    # creamos otra prueba:

    def test_show_return_200_whit_products(self):
        url = reverse("list_product")
        Product.objects.create(  # -> creamos un producto
            name="test", description="test description", price="5", available=True
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 1)
