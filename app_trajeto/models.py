from django.db import models

# Modelos: representam objetos que são mapeados para entidades no banco de dados
# Create your models here.

# Aramazena as sugestões de usuários
class Sugestao(models.Model):
    nome = models.CharField(max_length=250, blank=False)
    email = models.EmailField(max_length=250, blank=False)
    sugestao = models.TextField(max_length=250, blank=False)
    
    def __str__(self):
        return self.email

# Armazena os bairros
class Bairro(models.Model):
    nome = models.CharField(max_length=100, blank=False,unique=True)
   
    def __str__(self):
        return self.nome

# Armazena os veículos
class Veiculo(models.Model):
    descricao = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.descricao

# Armazena trajetos
class Trajeto(models.Model):
   
    SAIDA_GARAGEM = (
        ('M', (str)('6:30')),
        ('T', (str)('12:00')),
        ('N', (str)('18:30')),
    )
    
    nome_trajeto = models.CharField(max_length=100, blank=False, null=False)
    saida_garagem = models.CharField(max_length=1, choices=SAIDA_GARAGEM)

    def __str__(self):
        return f'Trajeto: {self.nome_trajeto} \n Saida Garagem: {self.saida_garagem}'
    
# Cadastra bairros em um trajeto definido
class Trajeto_Bairro(models.Model):
    trajeto = models.ForeignKey(Trajeto, on_delete = models.CASCADE)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete = models.CASCADE)
    
    class Meta:
        unique_together = ('trajeto','bairro','veiculo')    
    
    def __str__(self):
        return f'{self.bairro}, {self.trajeto.saida_garagem}'
    