from django.db import models
from django.conf import settings
from django.utils import timezone


class Banco(models.Model):
    nome = models.CharField("Nome", max_length=200, help_text="Insira Nome do Usuário",null=False)
    saldo = models.IntegerField("Saldo", max_length=100,null=True)
    recarga = models.IntegerField("Recarga", max_length=100, help_text="Insira valor da Recarga",null=True)
    numero = models.IntegerField("Número de Bilhetes", max_length=100,null=True)
    data_compra = models.DateTimeField(default=timezone.now,null=True)
    
    

    def publish(self):
        self.data_encontro = timezone.now()
        self.save()
