from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')


def contato(request):
    contato = {}
    contato['email'] = request.POST.get('email')
    contato['nome'] = request.POST.get('nome')
    contato['sobrenome'] = request.POST.get('sobrenome')
    contato['endereco'] = request.POST.get('endereco')
    contato['receber-noticias'] = request.POST.get('receber-noticias')
    contato['mensagem'] = request.POST.get('mensagem')
    return render(request, 'website/contato.html')


def servicos(request):
    return render(request, 'website/servicos.html')

  
def sobre(request):
  return render(request, 'website/sobre.html')


def plano(request):
  return render(request, 'website/plano.html')
