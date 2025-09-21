from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'loja/lista_produtos.html', {'produtos': produtos})



from django.shortcuts import get_object_or_404
from .models import Pedido

def rastrear_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'loja/rastrear_pedido.html', {'pedido': pedido})