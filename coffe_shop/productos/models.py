from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField(
        max_length=200, verbose_name="nombre"
    )  # ---> el verbose_name se usa para nombrar el campo
    #  y mostrarlo como queremos
    description = models.TextField(max_length=200, verbose_name="descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="foto"
    )
    # --> argumento donde especifica donde se sube la foto
    # --> permitimos que se puedan cargar productos sin foto con los otros argumentos
    # --> ponemos nombre al campo 'foto'

    def __str__(self):
        return self.name
