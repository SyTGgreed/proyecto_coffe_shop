from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):

    class Meta:  # debemos pasarle un modelo
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "available",
            "photo",
        ]
