"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from miapp.views import articulos, borrararticulo, creararticulo, editararticulo, formulario, hola_mundo, index, makearticulo, pordefecto, redireccionar, sacararticulo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('hola/',hola_mundo,name="hola"),
    path('index/',redireccionar,name="redireccionar"),
    path('pordefecto/<str:parametro>/',pordefecto,name="pordefecto"),
    path('crear-articulo/<str:title>/<str:content>/<str:published>/',creararticulo,name="crear_articulo"),
    path('articulo',sacararticulo,name="sacar_articulo"),
    path('edit/<int:id>/',editararticulo,name="editar_articulo"),
    path('articulos/',articulos,name="articulos"),
    path('borrar/<int:id>/',borrararticulo,name="borrar"),
    path('formulario/',formulario,name="formulario"),
    path('makearticulo/',makearticulo,name="makearticulo"),
]
