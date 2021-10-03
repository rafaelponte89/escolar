from app_trajeto.models import Sugestao, Bairro
from django import forms
import string
    
class Contato(forms.ModelForm):
    nome = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True)
    sugestao = forms.CharField( max_length=250, required=True )
    nome.widget.attrs.update({'class':'validate'})
    email.widget.attrs.update({'class':'validate'})
    sugestao.widget.attrs.update({'class':'validate'})
    
    class Meta:
        model = Sugestao
        fields = [ 'nome', 'email', 'sugestao']

