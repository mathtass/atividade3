from django.shortcuts import render
from .models import Banco
import pdb

# Create your views here.
def home(request):
    nome = ""
    banco = Banco.objects.all().order_by('nome')
    if request.method=='POST':
        nome = request.POST['name']
        banco = Banco.objects.filter(nome=nome)
        if (banco):
            print("tem nome")
        else:
            Banco.objects.create(nome=nome,saldo=0,numero=0)
    return render(request, 'aplicativo/home.html', {'banco': banco, 'nome':nome})


def recarga(request):
    if request.method=='POST':
        nome = request.POST['name']
        recarga = request.POST['recarga']
        busca = Banco.objects.filter(nome=nome)
        saldo_atual = int(recarga) + busca[0].numero
        busca[0].saldo = saldo_atual
        Banco.objects.filter(nome=nome).update(saldo=saldo_atual)
    return render(request, 'aplicativo/recarga.html')
