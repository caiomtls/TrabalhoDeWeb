from ast import For
from django.contrib import admin

from .models import Produto
from .models import Cliente
from .models import Compra
from .models import Fornecedor
from .models import Venda
from .models import Vendedor


admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Fornecedor)
admin.site.register(Venda)
admin.site.register(Vendedor)
