from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from . import models

@csrf_exempt
def login2(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(username=username, password=senha)

        import pika
        credentials = pika.PlainCredentials('guest', 'guest')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))

        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)

        if user:
            message = "O usuário com nome " + username + " logou"
        else:
            message = "O usuário com nome " + username + " tentou logar"
        
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        connection.close()

        if user:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

def index2(request):
    if request.user.is_authenticated:
        produtos = models.Produto.objects.all()
        return render(request, 'index.html', {"dados": produtos})
    else: return redirect('login')

def clientes(request):
    if request.user.is_authenticated:
        clientes = models.Cliente.objects.all()
        return render(request, 'clientes.html', {"dados": clientes})
    else: return redirect('login')

def vendas(request):
    if request.user.is_authenticated:
        vendas = models.Venda.objects.all()
        return render(request, 'produtos.html', {"dados":vendas})
    else: return redirect('login')

def fornecedores(request):
    if request.user.is_authenticated:
        fornecedores = models.Fornecedor.objects.all()
        return render(request, 'fornecedores.html', {"dados": fornecedores})
    else: return redirect('login')

def pedidos(request):
    if request.user.is_authenticated:
        pedidos = models.Compra.objects.all()
        return render(request, 'pedidos.html', {"dados": pedidos})
    else: return redirect('login')
