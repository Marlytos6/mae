import re
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import User

def password_is_valid(request, password, confirm_password):
    if len(password) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        return False

    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False

    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
        return False

    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
        return False

    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False
        
    return True

def user_is_valid(request, user, email):
    usuario = User.objects.filter(username= user)
    mail = User.objects.filter(email= email)
    if len(user) == 0 or len(email) == 0:
        messages.add_message(request, constants.ERROR, 'Usuário ou Email vazio')
        return False
    
    if len(usuario) != 0:
        messages.add_message(request, constants.ERROR, 'Usuário já cadastrado')
        return False
    
    if len(mail) != 0:
        messages.add_message(request, constants.ERROR, 'Email já cadastrado')
        return False
    return True
