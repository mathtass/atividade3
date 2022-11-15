from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recarga', views.recarga, name='recarga'),
]