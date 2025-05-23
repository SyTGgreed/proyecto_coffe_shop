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

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("productos.urls")),  # incluimos urls de app productos
    path("admin/", admin.site.urls),
    path("usuarios/", include("users.urls")),  # incluimos urls de app users
    path("pedidos/", include("orders.urls")),  # incluimos urls de app orders
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # static() --> para obtener la url de los archivos estaticos
# recibe como parametros la configuracion que tenemos de los archivos estaticos y de media
# importando settings
