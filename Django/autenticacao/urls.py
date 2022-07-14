from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastrar, name='cadastro'),
]
