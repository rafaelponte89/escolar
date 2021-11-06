from app_trajeto.models import Sugestao, Bairro
from django import forms

    
# Define um objeto contato para ser salvo no banco de dados
class Contato(forms.ModelForm):
    nome = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True)
    sugestao = forms.CharField( max_length=250, required=True )
    
    # atribui propriedades à página html em sua geração, no caso aquelas propriedades recebem as respectivas classes css
    nome.widget.attrs.update({'class':'validate'})
    email.widget.attrs.update({'class':'validate'})
    sugestao.widget.attrs.update({'class':'validate'})
    
    class Meta:
        model = Sugestao
        fields = [ 'nome', 'email', 'sugestao']

