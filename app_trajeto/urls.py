from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# rotas, ligação entre o endereço, a view chamada e o template

urlpatterns = [
    path("inicial",views.index,name="inicial"),            # endereco, view, nome da view
    path("quemsomos",views.quem_somos,name="quemsomos"),
    path("contato", views.salva_sugestoes, name="contato"),
    path("bairros",views.lista_bairros, name="bairro"),
    path("detail/<str:busca>", views.detalha_trajetos, name="detalha_trajetos"),

    # -------------EM DESENVOLVIMENTO --------------
    path("mapa/<str:bairro>", views.pontos_interesse, name="pontos_interesse"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

