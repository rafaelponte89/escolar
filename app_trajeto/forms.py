from app_trajeto.models import Sugestao, Bairro, Ponto
from django import forms



def select_bairros():
    bairros = Bairro.objects.order_by("nome").all().values('id','nome')
    lista_bairros = []
    lista_tupla = []
    for i in bairros:
        lista_bairros.append(i)

    for i in lista_bairros:
        lista_tupla.append((i["id"],i["nome"]))

    return lista_tupla

# Define um objeto contato para ser salvo no banco de dados

class Contato(forms.ModelForm):
    nome = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True)
    sugestao = forms.CharField(widget=forms.Textarea(), max_length=250, required=True )
    # atribui propriedades à página html em sua geração, no caso aquelas propriedades recebem as respectivas classes css
    nome.widget.attrs.update({'class':'validate','tabindex':1,'id':'nome'})
    email.widget.attrs.update({'class':'validate','tabindex':2,'id':'email'})
    sugestao.widget.attrs.update({'class':'validate' ,'tabindex':3,'id':'sugestao'})
    
    class Meta:
        model = Sugestao
        fields = [ 'nome', 'email', 'sugestao']


#----------------------------EM DESENVOLVIMENTO -------------
# Define um ponto para ser salvo no banco de dados
class formPonto(forms.ModelForm):

    BAIRROS = select_bairros()
    lat = forms.FloatField(required=True);
    lon = forms.FloatField(required=True)

    des = forms.CharField(widget=forms.Textarea(),max_length=150, required=True)
    hr = forms.CharField(max_length=2, required=True)
    mn = forms.CharField(max_length=2, required=True)
    
    # atribui propriedades à página html em sua geração, no caso aquelas propriedades recebem as respectivas classes css
    lat.widget.attrs.update({'id': 'latitude','readonly':'true'})
    lon.widget.attrs.update({'id': 'longitude','readonly':'true'})
    des.widget.attrs.update({'class': 'validate', 'tabindex': 1})
    hr.widget.attrs.update({'class': 'validate', 'tabindex': 2})
    mn.widget.attrs.update({'id':'id_min','class': 'validate', 'tabindex': 3})
    
   

    class Meta:
        model = Ponto
        fields = ['lat', 'lon', 'des','hr','mn',]

