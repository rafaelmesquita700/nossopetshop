from django.shortcuts import render
from django.shortcuts import redirect

def produtos(request):
    if request.session.get('usuario'):
        return render(request, 'Produtos.html')
    else:
        return redirect('/login/?status=2')

def categorias(request):
    if request.session.get('usuario'):
        return render(request, 'categorias.html')
    else:
        return redirect('/login/?status=2')

def compra(request):
    if request.session.get('usuario'):
        return render(request, 'telaCompra.html')
    else:
        return redirect('/login/?status=2')