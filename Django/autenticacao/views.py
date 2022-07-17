from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth
import os
from django.conf import settings
from .models import Ativacao
from hashlib import sha256
from . import utils

# Create your views here.
def login(request):
    return render(request, 'login.html')

@csrf_exempt
def cadastrar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'registrar.html')
    elif request.method == 'POST':
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar_senha')
        if not utils.password_is_valid(request, senha, confirmar):
            return redirect('/auth/cadastro/')
        if not utils.user_is_valid(request, username, email):
            return redirect('/auth/cadastro')
        # tratar exceções
        # criar uma tabela e salvar no banco de dados
        # criar um token e salvar no respectivo user
        # enviar mensagem por email
        # mensagem de sucesso
        # redirecionar ao site
        return HttpResponse(username)

def sair(request):
    auth.logout(request)
    return redirect('/auth/logar/')