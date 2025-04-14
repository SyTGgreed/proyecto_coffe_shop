"""
URL configuration for coffe_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ListProductsViews, ProductFormView, success, ProductListAPI



urlpatterns = [
    path('list_products/', ListProductsViews.as_view(), name='list_product'), #el name se utiliza para referenciar en el archivo html
    path('agregar/', ProductFormView.as_view(), name='add_products'),
    path('productos_agregados/',success.as_view(), name='success'),
    path('api/',ProductListAPI.as_view() , name='add_product'),

]