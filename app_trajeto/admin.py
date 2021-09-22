from app_trajeto.models import Bairro, Sugestao, Veiculo, Trajeto
from django.contrib import admin

# Register your models here.

admin.site.register(Sugestao)
admin.site.register(Bairro)
admin.site.register(Veiculo)
admin.site.register(Trajeto)