from django.db import models

# Create your models here.

class Regiao(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)


    def _str_(self):
        return self.nome


class Praia(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to = 'praia', null = True, blank = True, default = None)
    regiao = models.ForeignKey(Regiao, on_delete = models.CASCADE, related_name = 'praia')
    servicos = models.ManyToManyField(Servico, related_name = 'praia')
    def _str_(self):
        return self.nome