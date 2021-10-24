from django.db import models


# Create your models here.
class Empreendedor(models.Model):
    nome = models.CharField(max_length=80)
    endereco = models.CharField(max_length=80)
    bairro = models.CharField(max_length=80)
    cidade = models.CharField(max_length=80)
    uf = models.CharField(max_length=2)
    whatsapp = models.CharField(max_length=11)
        
    #id_usuario = models.ForeignKey()
