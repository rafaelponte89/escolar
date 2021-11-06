from django.template import context
from app_trajeto.models import Bairro, Trajeto_Bairro
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, QueryDict
from django.core.paginator import Paginator
from . forms import Contato
from django.contrib import messages
# Create your views here.

# Local destinado a lógica do negócio, definição do template a ser utilizado

# chama página index
def index(request):
    return render(request,"app_trajeto/index.html")    

# chama página quemsomos
def quem_somos(request):
    return render(request, "app_trajeto/quemsomos.html")
          
# chama página faleconosco
def fale_conosco(request):
    return render(request, "app_trajeto/faleconosco.html")

# salva sugestao sobre a pagina contato através de um formulário e método post
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

# lista todos os bairros, pode pesquisar o bairro também
def list_bairro(request):
    bairros = Bairro.objects.order_by("nome").all().values('nome')
    
    busca = request.GET.get('search', '')
    
    if busca:
        bairros = bairros.filter(nome__contains=busca).values('nome')
    
    #print(str(bairros.query))
    return render(request, 'app_trajeto/bairro.html', {'bairros':bairros,'busca':busca})

# mostra os trajetos cadastrados no bairro que foi selecionado
def detail_trajeto(request,busca):


    procurar = request.GET.get('search', '')
    trajetos = Trajeto_Bairro.objects.filter(bairro__nome__contains=busca).only('trajeto_id')
    print(str(trajetos.query))
    if procurar:
        trajetos = trajetos.filter(trajeto_id__saida_garagem__contains=procurar)
        #print(str(trajetos.query))

    return render (request, 'app_trajeto/detail_trajetos.html',{'trajetos':trajetos,'bairro':busca})

# pesquisa por período M,T,N
def search_trajeto(request):

    busca = request.GET.get('search', '')
    if busca:
        trajetos = Trajeto_Bairro.objects.filter(bairro__nome__contains=busca).only('trajeto_id')
    # print(str(trajetos.query))
    
    return render (request, 'app_trajeto/detail_trajetos.html',{'trajetos':trajetos,'bairro':busca})
   


# modificado
def trajetos(request):  
    trajetos_bairros = Trajeto_Bairro.objects.all()
    busca = request.GET.get('search', '')
    if busca:
        trajetos_bairros = trajetos_bairros.filter(bairro__nome__contains=busca)

    #paginator = Paginator(trajetos, 2)
    #page = request.GET.get('page',1)
    #page_obj = paginator.page(page)
    for trajeto in trajetos_bairros:
        print(trajeto.trajeto.saida_garagem)
        print(trajeto.bairro)

    return render(request, 'app_trajeto/trajetos.html', {'trajetos':trajetos_bairros,'busca': busca })   

    



    

