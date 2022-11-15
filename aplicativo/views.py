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
        saldo_atual = int(recarga) + busca[0].saldo
        busca[0].saldo = saldo_atual
        Banco.objects.filter(nome=nome).update(saldo=saldo_atual)
    return render(request, 'aplicativo/recarga.html')


def comprar_bilhete(request):
    nome = ""
    banco = Banco.objects.all().order_by('nome')
    compra =  ''
    if request.method=='POST':
        nome = request.POST['name']
        bilhetes = request.POST['bilhetes']
        banco = Banco.objects.filter(nome=nome)
        preco = int(bilhetes) * int(3)
        if (int(banco[0].saldo) > int(preco)):
            numero_bilhetes = int(bilhetes) + banco[0].numero
            saldo_atual = int(banco[0].saldo) - 3
            Banco.objects.filter(nome=nome).update(numero=numero_bilhetes,saldo=saldo_atual)  
            compra = 'true'
        else:
            compra = 'false'
    return render(request, 'aplicativo/comprar_bilhete.html', {'banco': banco, 'nome':nome, 'compra':compra})


def usar_bilhete(request):
    pass