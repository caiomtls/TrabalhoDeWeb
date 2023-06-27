from django.contrib.auth.decorators import user_passes_test

def is_vendedor(user):
    return user.groups.filter(name='Vendedor').exists()

def is_estoque(user):
    return user.groups.filter(name='Estoque').exists()

def is_gerente(user):
    return user.groups.filter(name='Gerente').exists()

# Decorator para verificar se o usuário é do grupo "Vendedor" ou é um administrador
def vendedor_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: is_vendedor(user) or is_gerente(user),
        login_url='index',
    )(view_func)
    return decorated_view_func

# Decorator para verificar se o usuário é do grupo "Estoque" ou é um administrador
def estoque_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: is_estoque(user) or is_gerente(user),
        login_url='index',
    )(view_func)
    return decorated_view_func
