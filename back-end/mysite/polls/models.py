from django.db import models


class Cliente(models.Model):
  # ID é criado automaticamente como PK
  nome = models.CharField(max_length=20)
  sobrenome = models.CharField(max_length=20)
  cpf = models.CharField(max_length=11, unique=True)
  telefone = models.CharField(max_length=11)
  email = models.EmailField(max_length=30)
  endereco = models.CharField(max_length=60)
  def __str__(self):
    return self.nome+" "+self.sobrenome

class Vendedor(models.Model):
  nome = models.CharField(max_length=20)
  sobrenome = models.CharField(max_length=20)
  cpf = models.CharField(max_length=11, unique=True)
  telefone = models.CharField(max_length=11)
  email =  models.EmailField(max_length=30)
  endereco = models.CharField(max_length=60)
  def __str__(self):
    return self.nome+" "+self.sobrenome

class Fornecedor(models.Model):
  nome = models.CharField(max_length=30)
  cnpj = models.CharField(max_length=15, unique=True)
  telefone = models.CharField(max_length=11)
  email =  models.EmailField(max_length=30)
  def __str__(self):
    return self.nome

class Produto(models.Model):
  nome = models.CharField(max_length=30)
  quantidade = models.IntegerField() # = Comprado - Vendido
  def __str__(self):
    return self.nome


class Venda(models.Model):
  STATUS = [
    ("FL", "Finalizada"),
    ("EM", "Em andamento"),
    ("CL", "Cancelada")
  ]
  id_produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
  id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
  id_vendedor = models.ForeignKey(Vendedor,on_delete=models.CASCADE)
  quantidade = models.IntegerField()
  valor_unitario = models.FloatField(max_length=10000000)
  status = models.CharField(max_length=2, choices=STATUS)
    

class Compra(models.Model):
  STATUS = [
    ("FL", "Finalizada"),
    ("EM", "Em andamento"),
    ("CL", "Cancelada")
  ]
  id_produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
  id_fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
  quantidade = models.IntegerField()
  valor_unitario = models.FloatField(max_length=10000000)
  status = models.CharField(max_length=2, choices=STATUS)
