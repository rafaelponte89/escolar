from django.template import context
from app_trajeto.models import Bairro, Trajeto_Bairro
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, QueryDict
from django.core.paginator import Paginator
from . forms import Contato
from django.contrib import messages
# Create your views here.


# um usuário decidi acessar o site para procurar pontos
# em seu bairro
def index(request):
    return render(request,"index.html")


# ao cliar na opção trajetos uma lista de bairros é exibida
# para o usuário
def lista_bairros(request):
    bairros = Bairro.objects.order_by("nome").all().values('nome')

    busca = request.GET.get('search', '')
    if busca:
        bairros = bairros.filter(nome__icontains=busca).values('nome')

    return render(request, 'bairro.html', {'bairros': bairros, 'busca': busca})

# aqui o usuário pode buscar por um bairro, digitando partes do nome, letras maiúsculas ou minúsculas
# os trajetos referentes ao bairro selecionado aparecem
# existe um tipo de filtragem por períodos que ao usar o usuário pode refinar sua pesquisa
def detalha_trajetos(request,busca):

    procurar = request.GET.get('search', '')
    trajetos = Trajeto_Bairro.objects.filter(bairro__nome__contains=busca).only('trajeto_id')

    if procurar:
        trajetos = trajetos.filter(trajeto_id__saida_garagem__contains=procurar)

    return render (request, 'detalha_trajetos.html',{'trajetos':trajetos,'bairro':busca})

# então o usuário decidi acessar a página fale_conosco
# para deixar sua experiência e sugestão com o site
def fale_conosco(request):
    return render(request, "faleconosco.html")


# após cliar no botão da página fale_conosco o usuário se depara com uma mensagem de sucesso
def salva_sugestoes(request):
    if request.method == "POST":
        form = Contato(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Sucesso')
            return redirect('contato')
    else:
        form = Contato(request.POST)
    return render(request, "contato.html", {"form": form})


# ainda querendo explorar mais sobre o site o usuário acessa a seção quem somos
# para saber sobre a história da empresa e após terminar a leitra fecha a página
def quem_somos(request):

    return render(request, "quemsomos.html")
          










    

