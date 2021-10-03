from django.template import context
from app_trajeto.models import Trajeto
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, QueryDict
from django.core.paginator import Paginator
from . forms import Contato
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,"app_trajeto/index.html")    

def quem_somos(request):
    return render(request, "app_trajeto/quemsomos.html")

def trajetos(request):
     
    trajetos = Trajeto.objects.all()
    busca = request.GET.get('search', '')
    
    if busca:
        trajetos = trajetos.filter(bairro__nome__contains=busca)

    #paginator = Paginator(trajetos, 2)
    #page = request.GET.get('page',1)
    #page_obj = paginator.page(page)

    return render(request, 'app_trajeto/trajetos.html', {'trajetos':trajetos,'busca': busca })   
        
    
def fale_conosco(request):
    return render(request, "app_trajeto/faleconosco.html")

def salvar_sugestao(request):
    if request.method == "POST":
        form = Contato(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Sucesso')
            return redirect('contato')
    else:
        form = Contato(request.POST)
    return render(request, "app_trajeto/contato.html", {"form": form})

    



    

