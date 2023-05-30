from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('clientes', views.clientes, name='clientes'),
    path('produtos', views.produtos, name='produtos'),
    path('fornecedores', views.fornecedores, name='fornecedores'),
    path('pedidos', views.pedidos, name='pedidos'),
    path("login", views.login, name="login"),

]