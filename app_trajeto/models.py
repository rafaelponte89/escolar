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
    
class Veiculo(models.Model):
    descricao = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.descricao

class Trajeto(models.Model):
    SAIDA_GARAGEM = (
        ('M', (str)('6:30')),
        ('T', (str)('12:00')),
        ('N', (str)('18:30')),
    )
    
    
    bairro = models.ForeignKey(Bairro, on_delete = models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete = models.CASCADE)
    saida_garagem = models.CharField(max_length=1, choices=SAIDA_GARAGEM)
    
    class Meta:
        unique_together = ('bairro','veiculo','saida_garagem')    
    
    def __str__(self):
        return (f"Bairro: {self.bairro}, Horário Saída Garagem: {self.saida_garagem}" )
    