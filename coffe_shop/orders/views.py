from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from .forms import OrderProductForm
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MyOrderView(LoginRequiredMixin,DetailView):  # heredamos de una vista generica de django
                        # ponemos como primer parametro LoginRequire para validar si el usuario esta logeado
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = 'order'   # cambiamos en nombre de la variable del contexto para utilizarla en el html

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first() # estamos obteniendo una orden que esta activa
                                # el filter devuelve una lista, para que sea un elemento debemos poner .first()

class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/create_order_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active = True,
            user = self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
    

    