"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#from HolaMundo import views
from HolaMundo.views import hola, index
from mascotasApp.views import mascotas

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('', views.hola, name='hola')
    path('', hola, name='hola'),
    path('index/', index),
    path('hola/', hola),
    path('mascotas/', mascotas),
    #path('mascotas2/', mascotas2),
]
