from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def servicos(request):
    return render(request, 'servico.html')

def contatos(request):
    return render(request, 'contatos.html')

def sobre(request):
    return render(request, 'sobre.html')
