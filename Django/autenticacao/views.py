from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'registrar.html')