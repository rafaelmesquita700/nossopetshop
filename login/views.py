from django.shortcuts import render
from django.shortcuts import redirect
from hashlib import sha256
from cadastro.models import Cadastro

def login(request):
    status = request.GET.get('status')
    return render(request, 'Login.html', {'status': status})

def validar_login(request):
    email = request.POST.get('e-mail')
    senha = str(request.POST.get('senha'))
    senha = sha256(senha.encode()).hexdigest()
    
    usuario = Cadastro.objects.filter(cad_email=email).filter(cad_senha=senha)
    if len(usuario) == 0:
        return redirect('/login/?status=1')
    else:
        request.session['usuario'] = usuario[0].cad_codigo
        return redirect('/') # leva para a pagina inicial
    
def sair(request):
    request.session.flush()
    return redirect('/login/')