from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
arquivo views, onde vai ficar a lógica da nossa aplicação, onde fica toda aquela parte onde recebemos uma request e retornamos uma response, logo pegar o nome do usuário e verificar se ele existe, ou um e-mail/senha válido/inválido todo esse processamento fica aqui.
'''

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return HttpResponse('login') # quando eu acessar no meu navegador a rota 'auth/login', ele deve me retornar a resposta 'login'
