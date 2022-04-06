from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cadastro(request):
    return HttpResponse('cadastro') # quando eu acessar no meu navegador a rota 'auth/cadastro', ele deve me retornar a resposta 'cadastro'  

