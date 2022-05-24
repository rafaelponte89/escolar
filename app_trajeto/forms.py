from app_trajeto.models import Sugestao, Bairro
from django import forms

    
# Define um objeto contato para ser salvo no banco de dados
class Contato(forms.ModelForm):
    nome = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True)
    sugestao = forms.CharField( max_length=250, required=True )
    
    # atribui propriedades à página html em sua geração, no caso aquelas propriedades recebem as respectivas classes css
    nome.widget.attrs.update({'class':'validate','tabindex':1})
    email.widget.attrs.update({'class':'validate','tabindex':2})
    sugestao.widget.attrs.update({'class':'validate' ,'tabindex':3})
    
    class Meta:
        model = Sugestao
        fields = [ 'nome', 'email', 'sugestao']

