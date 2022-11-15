from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recarga', views.recarga, name='recarga'),
    path('comprar_bilhete', views.comprar_bilhete, name='comprar_bilhete'),
    path('usar_bilhete', views.usar_bilhete, name='usar_bilhete'),
    path('clientes', views.clientes, name='clientes'),
]