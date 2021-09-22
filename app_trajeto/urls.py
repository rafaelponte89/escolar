from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path("inicial",views.index,name="inicial"),
    path("quemsomos",views.quem_somos,name="quemsomos"),
    path("trajetos",views.trajetos, name="trajetos"),
    path("contato", views.salvar_sugestao, name="contato"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

