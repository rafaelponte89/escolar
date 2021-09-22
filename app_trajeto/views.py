from app_trajeto.models import Sugestao
from django.shortcuts import render, redirect
from . forms import Contato
# Create your views here.


def index(request):
    return render(request,"app_trajeto/index.html")    

def quem_somos(request):
    return render(request, "app_trajeto/quemsomos.html")

def trajetos(request): 
    return render(request, "app_trajeto/trajetos.html")

def fale_conosco(request):
    return render(request, "app_trajeto/faleconosco.html")

def salvar_sugestao(request):
    if request.method == "POST":
        form = Contato(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicial')
    else:
        form = Contato(request.POST)
    return render(request, "app_trajeto/contato.html", {"form": form})





    

