from django.shortcuts import render
from django.urls import reverse_lazy

from productos.forms import ProductForm


from .models import Product
from django.views.generic import TemplateView
from django.views import generic

# Create your views here.

class ListProductsViews(generic.ListView):    # lista generica ListView
                            # nos permite tener un modelo, un template y cambiar el nombre de la variable que estara
                                # en el contexto
    model = Product
    template_name = "productos/productos.html"
    context_object_name = 'products'

    
#Django nos proporciona varias vistas genericas
# una de ellas es form.view que importamos desde generic

class ProductFormView(generic.FormView):
    template_name = "productos/add_product.html"  #el formview ademas de el template requiere un formulario
    form_class = ProductForm
    success_url = reverse_lazy('success') # cuando el producto se cree, haga un redireccionamiento a la url especificada
                # el reverse_lazy se utiliza en la vista para añadir una url

    # creamos la funcion para la creacion del producto con el formulario
    def form_valid(self, form):  # recibe el formulario
        form.save()         # form.save() ejecuta el query que hace el guardado 
        return super().form_valid(form)
    
class success(TemplateView):
    template_name='productos/success.html'

    def success(request):
        all_products = Product.objects.all() # .objects.all() obtiene todos los atributos de Product

        return render(request,'success.html',{'products':all_products})
    
    


        




