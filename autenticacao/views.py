from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
'''
arquivo views, onde vai ficar a lógica da nossa aplicação, onde fica toda aquela parte onde recebemos uma request e retornamos uma response, logo pegar o nome do usuário e verificar se ele existe, ou um e-mail/senha válido/inválido todo esse processamento fica aqui.
'''

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        print (f"{username}|{senha}|{confirmar_senha}")
        
        #validações para o cadastro
        if not senha == confirmar_senha:
            print("erro de senha diferente da confirmação")
            return redirect("/auth/cadastro")
        if len(username.strip())==0 or len(senha.strip())==0:
            print("user/senha vazios")
            return redirect("/auth/cadastro")
        user = User.objects.filter(username = username)
        if user.exists() :
            print(f"erro de usuário {username} já cadastrado")
            return redirect("/auth/cadastro")
        
        #tentando preencher o BD
        try:
            user=User.objects.create_user(username=username, password = senha)
            user.save()

            return redirect("/auth/login")
        except:
            return redirect("/auth/cadastro")



        return HttpResponse('Recebido')

def login(request):
    return HttpResponse('login') # quando eu acessar no meu navegador a rota 'auth/login', ele deve me retornar a resposta 'login'
