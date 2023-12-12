from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import *

#cadastro do usuário da aplicação
def cad_user(request):
    if request.method == 'POST':
        form_usuarios = UserCreationForm(request.POST)
        if form_usuarios.is_valid():
            form_usuarios.save()
            return redirect('index')
    else:
        form_usuarios = UserCreationForm()
    return render(request, 'cadastrar_usuarios.html', {'form_usuarios': form_usuarios})

#fazer login na aplicação
def log_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username = username, password = password)
        if usuario is not None:
            login(request, usuario)
            return redirect('pagina_principal')
        else:
            form_logins = AuthenticationForm()
    else:
        form_logins = AuthenticationForm()
    return render(request, 'login_usuarios.html', {'form_logins': form_logins})  

def index(request):
    return render(request, "index.html")