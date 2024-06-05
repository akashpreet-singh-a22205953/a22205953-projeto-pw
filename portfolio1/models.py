from django.db import models



class Intro(models.Model):
    intro = models.CharField(max_length=200)

    def __str__(self):
        return self.intro

class MeByMe(models.Model):
    about = models.CharField(max_length = 500)
    interesses = models.CharField(max_length = 1000,default="Habilidades a serem adicionadas")
    aptidoes = models.CharField(max_length=500, default="Habilidades a serem adicionadas")
    competencias = models.CharField(max_length = 500,default="a serem adicionadas")
    experiencia = models.CharField(max_length = 5000,default="a serem adicionadas")
    cv = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.about

class TechPresentation(models.Model):
    introduction = models.TextField(max_length=2000)
    technologies = models.TextField(max_length=2000)
    django_hands_on_video = models.URLField(max_length=200)
    project_tour_video = models.URLField(max_length=200)

    def __str__(self):
        return self.introduction

class allApp(models.Model):
    Bnadas = models.ImageField(upload_to='images/', null=True, blank=True)
    Lei = models.ImageField(upload_to='images/', null=True, blank=True)
    Artigos = models.ImageField(upload_to='images/', null=True, blank=True)
    Meteo = models.ImageField(upload_to='images/', null=True, blank=True)

