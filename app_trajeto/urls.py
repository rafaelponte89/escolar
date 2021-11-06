from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# rotas, ligação entre o endereço, a view chamada e o template

urlpatterns = [
    path("inicial",views.index,name="inicial"),            # endereco, view, nome da view
    path("quemsomos",views.quem_somos,name="quemsomos"),
    path("contato", views.salvar_sugestao, name="contato"),
    path("bairros",views.list_bairro, name="bairro"),
    path("detail/<str:busca>", views.detail_trajeto, name="detail"),
    path("trajetos",views.trajetos, name="trajetos"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

