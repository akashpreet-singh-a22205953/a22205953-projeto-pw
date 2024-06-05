

from django.db import models

class Curso(models.Model):
    apresentacao = models.CharField(max_length=50)
    objectivos = models.CharField(max_length=50)
    competencias = models.CharField(max_length=50)

    def __str__(self):
        return f"Apresentação: {self.apresentacao} objectivos: {self.objectivos} competencias: {self.competencias}"


class area_Cientifica(models.Model):
    area = models.CharField(max_length=50)

    def __str__(self):
        return f"Area: {self.area} "

class disciplina(models.Model):
    nome= models.CharField(max_length=50)
    ano= models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    curricular_IUnit_Readable_Code = models.CharField(max_length=50)

    def __str__(self):
        return f"Disciplina: {self.nome}, ano: {self.ano}, semestre: {self.semestre}, ects: {self.ects}, Codigo: {self.curricular_IUnit_Readable_Code} "

class projeto(models.Model):
    projeto = models.CharField(max_length=50)
    disciplina = models.CharField(max_length=50)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.CharField(max_length=50)
    conceitos_aplicados = models.CharField(max_length=50)
    link_video = models.CharField(max_length=50)
    link_gitHub = models.CharField(max_length=50)

    def __str__(self):
        return f"Nome {self.projeto} desenvolvido na cadeira de {self.disciplina} em {self.ano}º ano, {self.semestre}º semestre, descrição:  {self.descricao}, conceitos: {self.conceitos_aplicados}, links: {self.link_video}, {self.link_gitHub} "


class Docente(models.Model):
    nome = models.CharField(max_length=50)
    disciplinas = models.ManyToManyField(disciplina)

    def __str__(self):
        return f"{self.nome} leciona: {self.disciplinas}"

class Linguagem_Programacao(models.Model):
    nome = models.CharField(max_length=50)
    disciplina = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} é usada nesta disciplina/projeto {self.disciplina} "