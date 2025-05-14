from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.


class MyOrderViewTests(TestCase):
    # prueba para verificar si un usuario NO esta logeado sea redireccionado al login
    def test_no_logged_user_should_redirect(self):
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # breakpoint() # detenemos el programa para saber la url ejecutando en la shell (PDB) response.url
        # revisar PDB y los comandos que pueden utilizar
        self.assertEqual(response.url, "/usuarios/login/?next=/pedidos/mi_orden")

        # prueba para verificar si un usuario eta logeado

    def test_logged_user_should_redirect(self):
        url = reverse("my_order")
        # debemos crear un usuario para poder realizar la prueba
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user)  # para no pasar contraseña utilizamos este metodo
        response = self.client.get(url)
        # breakpoint() # detenemos el programa para saber la url ejecutando en la shell (PDB) response.url
        # revisar PDB y los comandos que pueden utilizar
        self.assertEqual(response.status_code, 200)
