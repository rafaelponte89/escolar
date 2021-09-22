from django.db import models

# Create your models here.

class Sugestao(models.Model):
    nome = models.CharField(max_length=250, blank=False)
    email = models.EmailField(max_length=250, blank=False)
    sugestao = models.TextField(max_length=250, blank=False)
    
    def __str__(self):
        return self.email
    
class Bairro(models.Model):
    nome = models.CharField(max_length=100, blank=False)
   
    def __str__(self):
        return self.nome
        
    
    