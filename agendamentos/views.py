from django.shortcuts import render
from django.shortcuts import redirect
from cadastro.models import Cadastro
from servicos.models import Banhoetosa, Consultas, Adestramento

# Create your views here.
def agendamentos(request):
    if request.session.get('usuario'):
        status = request.GET.get('status')

        usuario = Cadastro.objects.filter(cad_codigo=request.session.get('usuario'))
        nome = usuario[0].cad_nome

        return render(request, 'Agendamentos.html', {'status': status, 'nome':nome})
    else:
        return redirect('/login/?status=2')

def processa_agendamento(request):
    if request.session.get('usuario'):
        servico = str(request.POST.get('radsex'))
        nome = str(request.POST.get('nomepet'))
        tipo = str(request.POST.get('tp'))
        raca = str(request.POST.get('raça'))
        responsavel = str(request.POST.get('responsavel'))
        dia = str(request.POST.get('dia'))
        hora = str(request.POST.get('hora'))
        
        if not nome.isalpha() or not tipo.isalpha() or not responsavel.isalpha():
            return redirect('/agendamentos/?status=2')
        
        if raca != '' and not raca.isalpha():
            return redirect('/agendamentos/?status=2')
        
        if dia == '' or hora  == "" or hora < '08:00' or hora > '17:00':
            return redirect('/agendamentos/?status=3')

        
        try:
            if servico == 'bt':
                servico = Banhoetosa(
                    bet_nomePet=nome, 
                    bet_tipoPet=tipo,
                    bet_raca=raca,
                    bet_responsavel=responsavel,
                    bet_dia=dia,
                    bet_hora=hora
                )
            elif servico == 'cm':
                servico = Consultas(
                    con_nomePet=nome, 
                    con_tipoPet=tipo,
                    con_raca=raca,
                    con_responsavel=responsavel,
                    con_dia=dia,
                    con_hora=hora
                )
            elif servico == 'ad':
                servico = Adestramento(
                    ade_nomePet=nome, 
                    ade_tipoPet=tipo,
                    ade_raca=raca,
                    ade_responsavel=responsavel,
                    ade_dia=dia,
                    ade_hora=hora
                )
            servico.save()
            return redirect('/agendamentos/?status=0')
        except:
            return redirect('/agendamentos/?status=1')
    else:
        return redirect('/login/?status=2')