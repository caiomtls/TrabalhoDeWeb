from django.shortcuts import redirect

class TipoUsuarioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.tipo == 'admin':
                return redirect('admin_dashboard')
            elif request.user.tipo == 'estoque':
                return redirect('estoque_dashboard')
            elif request.user.tipo == 'vendedor':
                return redirect('vendedor_dashboard')

        return self.get_response(request)
