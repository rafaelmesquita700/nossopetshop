from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cadastro
from hashlib import sha256

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'Cadastro.html', {'status': status})

def processa_cadastro(request):
    nome = str(request.POST.get('CAD_NOME'))
    email = str(request.POST.get('CAD_EMAIL'))
    rua = str(request.POST.get('CAD_RUA'))
    numero = str(request.POST.get('CAD_NUMERO'))
    bairro = str(request.POST.get('CAD_BAIRRO'))
    cidade = str(request.POST.get('CAD_CIDADE'))
    contato = str(request.POST.get('CAD_CONTATO'))
    senha = str(request.POST.get('CAD_SENHA'))
    
    if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(rua.strip()) == 0 or len(numero.strip()) == 0 
        or len(bairro.strip()) == 0 or len(cidade.strip()) == 0):
        return redirect('/cadastro/?status=3')

    if not nome.isalpha() or not rua.isalpha() or not bairro.isalpha() or not cidade.isalpha():
        return redirect('/cadastro/?status=4')
    
    cadastro = Cadastro.objects.filter(cad_email=email)
    if len(cadastro) > 0:
        return redirect('/cadastro/?status=0')
    else:
        try:
            senha = sha256(senha.encode()).hexdigest()
            cadastro = Cadastro(
                cad_nome=nome, 
                cad_email=email, 
                cad_rua=rua,
                cad_numero=numero,
                cad_bairro=bairro,
                cad_cidade=cidade,
                cad_contato=contato,
                cad_senha=senha
            )
            cadastro.save()
            return redirect('/cadastro/?status=1')
        except Exception as e:
            print(e)
            return redirect('/cadastro/?status=2')