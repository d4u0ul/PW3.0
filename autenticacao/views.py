from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
# Create your views here.
'''
arquivo views, onde vai ficar a lógica da nossa aplicação, onde fica toda aquela parte onde recebemos uma request e retornamos uma response, logo pegar o nome do usuário e verificar se ele existe, ou um e-mail/senha válido/inválido todo esse processamento fica aqui.
'''

def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/plataforma')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        print (f"{username}|{senha}|{confirmar_senha}")
        
        #validações para o cadastro
        if not senha == confirmar_senha:
            messages.add_message(request,constants.ERROR, 'As senhas não coincidem')
            print("erro de senha diferente da confirmação")
            return redirect("/auth/cadastro")
        if len(username.strip())==0 or len(senha.strip())==0:
            messages.add_message(request,constants.ERROR, 'user/senha vazios')
            print("user/senha vazios")
            return redirect("/auth/cadastro")
        user = User.objects.filter(username = username)
        if user.exists() :
            messages.add_message(request,constants.ERROR, f"erro de usuário {username} já cadastrado")
            print(f"erro de usuário {username} já cadastrado")
            return redirect("/auth/cadastro")
        
        #tentando preencher o BD
        try:
            user=User.objects.create_user(username=username, password = senha)
            user.save()

            return redirect("/auth/login")
        except:
            
            messages.add_message(request,constants.ERROR, 'erro interno do sistema')
            return redirect("/auth/cadastro")



        return HttpResponse('Recebido')

def login(request):
    #return HttpResponse('login') # quando eu acessar no meu navegador a rota 'auth/login', ele deve me retornar a resposta 'login'
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/plataforma')
        return render(request,"login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("password")
        
        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request,constants.ERROR, 'usuário ou senha inválidos')
            return redirect("/auth/login")
        else:
            auth.login(request, usuario)
            return redirect("/plataforma")

         
def sair(request):
    auth.logout(request)
    return redirect('/auth/login')
