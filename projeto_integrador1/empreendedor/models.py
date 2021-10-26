from django.db import models
from django.utils.timezone import now
#importa o model User do app Auth
from django.contrib.auth.models import User


# Create your models here.
class Empreendedor(models.Model):
    nome = models.CharField(max_length=80)  # nome completo do empreendedor
    endereco = models.CharField(max_length=80)  # nome da rua, logradouto
    bairro = models.CharField(max_length=80)  # nome do bairro
    cidade = models.CharField(max_length=80)  # nome da cidade
    uf = models.CharField(max_length=2)  # estado, tipo SP, MG, etc
    whatsapp = models.CharField(max_length=11)  # número do whatsapp
    # codigo do usuario vinculado no modulo auth
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # data da criação do empreendedor
    created_at = models.DateTimeField(auto_now_add=True)
    # data da última atualização do empreendedor
    updated_at = models.DateTimeField(auto_now=True)
    
class Categoria(models.Model)    :
    #id do empreendedor
    empreendedor = models.ForeignKey(Empreendedor,on_delete=models.CASCADE)
    #nome da categoria
    nome = models.CharField(max_length=80) 
    #R= receita / D= Despesa, guarda o tipo de categoria
    receita_despesa = models.CharField(max_length=1, default='D')
    #F= despesas fixa / V = despesa variável
    fixo_variavel = models.CharField(max_length=1, default='F')
    
class Lancamento(models.Model):
    #id do empreendedor
    empreendedor = models.ForeignKey(Empreendedor, on_delete=models.CASCADE)
    #nome do fornecedor ou cliente
    nome_fornecedor = models.CharField(max_length=80)
    #data do vencimento da despesa
    data_vencimento = models.DateTimeField(default=now, blank=True)
    #data do pagamento da despesa da despesa
    data_pagamento = models.DateTimeField(default=now, blank=True)
    #valor do lancamento
    valor = models.FloatField(default=0)
    #descricao / historico do lancamento
    descricao = models.TextField()
    #id da categoria
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
