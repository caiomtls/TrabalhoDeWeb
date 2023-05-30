from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def clientes(request):
    return render(request, 'clientes.html', {"nome":"Clientes", "tabela_Prop": ["ID","Nome","Email", "Telefone"],"dados":[
        {"id":"1","nome":"Doe","email":"john@example.com","telefone":"(32)93123-8831",},
        {"id":"2","nome":"Moe","email":"mary@example.com","telefone":"(12)93533-8512"},
        {"id":"3","nome":"Dooley","email":"july@example.com","telefone":"(16)94223-3838"}]})

def produtos(request):
    return render(request, 'produtos.html', {"nome":"Produtos", "tabela_Prop": ["ID","Nome","Quantidade", "Preço"],"dados":[
        {"id":"1","nome":"Pão","quantidade":"3","preco":"5,50",},
        {"id":"2","nome":"Danone","quantidade":"5","preco":"2,90"},
        {"id":"3","nome":"Bombom","quantidade":"7","preco":"1,50"}]})

def fornecedores(request):
    return render(request, 'fornecedores.html')

def pedidos(request):
    return render(request, 'pedidos.html')

# def index(request):
#     return render(request, 'teste.html', {"nome":"aaaa", "trails":["a","b","c", "d"]})