

from django import forms

from .models import Product


#### colocar las mismas especificaciones que estan en el modelo

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='nombre')  # campo nombre
    description = forms.CharField(max_length=300, label='descripcion')  # campo descripcion
    price = forms.DecimalField(max_digits=10,decimal_places=2, label='precio') # campo precio
    available = forms.BooleanField(initial=True, label='Disponible', required=False) #--> para mostrar el campo de un 
                                    #formulario inicialmente activo usamos initial=true, y el parametro required
                                    # si es requerido
    photo = forms.ImageField(label='foto', required=False)

    #creamos una funcion para guardar los datos

    def save(self):
        Product.objects.create(

            # los formularios tienen un diccionario que se llama cleaned_data que traen la informacion
            # limpia desde el request que hace el usuario cuando hace submit en el navegador
            name = self.cleaned_data['name'],
            description = self.cleaned_data['description'],
            price = self.cleaned_data['price'],
            available = self.cleaned_data['available'],
            photo = self.cleaned_data['photo'],
            
        )

