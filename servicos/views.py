from django.shortcuts import render
from django.shortcuts import redirect

def servicos(request):
    if request.session.get('usuario'):
        return render(request, 'Servicos.html')
    else:
        return redirect('/login/?status=2')