from django.urls import path

from . import views

urlpatterns = [
    path("", views.index2, name="index"),
    path("clientes", views.clientes, name="clientes"),
    path("vendas", views.vendas, name="vendas"),
    path("fornecedores", views.fornecedores, name="fornecedores"),
    path("pedidos", views.pedidos, name="pedidos"),
    path("login", views.login2, name="login"),
    path("logout", views.logout_view, name="logout"),
]
