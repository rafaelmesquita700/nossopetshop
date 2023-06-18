from django.shortcuts import render

def inicio(request):
    status = "Entrar"
    nome = ""
    return render(request, 'Inicio.html', {'status': status, 'nome': nome})

def contatos(request):
    return render(request, 'Contatos.html')



