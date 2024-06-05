from django.db import models

class Localizacao(models.Model):
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.cidade

class Banda(models.Model):
    nome = models.CharField(max_length=100)


    def __str__(self):
        return self.nome



class Festival(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, related_name='festivais')
    bandas = models.ManyToManyField(Banda, blank=True)
    foto = models.ImageField(upload_to='festivais/', null=True, blank=True)


    def __str__(self):
        return self.nome
