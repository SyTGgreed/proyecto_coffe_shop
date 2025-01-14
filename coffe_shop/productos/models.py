from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name='nombre')  #---> el verbose_name se usa para nombrar el campo 
                                                                    #  y mostrarlo como queremos
    description = models.TextField(max_length=200, verbose_name='descripcion')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precio')  