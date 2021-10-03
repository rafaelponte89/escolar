from app_trajeto.models import Bairro, Sugestao, Veiculo, Trajeto
from django.contrib import admin

# Register your models here.


#admin.site.register(Sugestao)

# exibe campos na página de administração, inclusão de filtros
@admin.register(Sugestao)
class SugestaoAdmin(admin.ModelAdmin):
    list_display = ('nome','email','sugestao')
    list_filter = ('nome',)
    

admin.site.register(Bairro)
admin.site.register(Veiculo)
admin.site.register(Trajeto)