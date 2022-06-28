from app_trajeto.models import Bairro, Ponto, Sugestao, \
    Veiculo,Trajeto, Trajeto_Bairro, Tipo_Transporte, \
        Ponto    

from django.contrib import admin

# Register your models here.


#admin.site.register(Sugestao)

# exibe campos na página de administração, inclusão de filtros
@admin.register(Sugestao)
class SugestaoAdmin(admin.ModelAdmin):
    list_display = ['nome','email','sugestao']
    list_filter = ['nome']
    search_fields = ['nome']
    list_per_page = 20
    
@admin.register(Bairro)
class Bairro(admin.ModelAdmin):
    list_filter = ['nome']
    list_per_page = 20
    search_fields = ['nome']



    
admin.site.register(Veiculo)
admin.site.register(Trajeto_Bairro)
admin.site.register(Trajeto)
admin.site.register(Tipo_Transporte)
admin.site.register(Ponto)