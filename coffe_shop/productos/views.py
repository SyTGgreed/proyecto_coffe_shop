from django.shortcuts import render
from .models import Product
from django.views.generic import TemplateView

# Create your views here.

class ListProductsViews(TemplateView):
    template_name = "coffe_shop/productos/coffe_shop/productos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context["list_products"] = products

        return context
        




