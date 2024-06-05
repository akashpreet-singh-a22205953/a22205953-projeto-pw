# loader.py

from biblioteca.models import *
import json

Autor.objects.all().delete()
Livro.objects.all().delete()

with open('biblioteca/json/autores.json') as f:
    autores = json.load(f)

    # autores é um dicionario de autores, tendo como
    # chave o nome do autor, e como
    # valor um dicionario com informação do autor  

    for autor, info in autores.items(): 
        Autor.objects.create(
            nome = autor,
            ano_nascimento = info['ano_nascimento'],
            nacionalidade = info['nacionalidade']
        )

with open('biblioteca/json/livros.json') as f:
    livros = json.load(f)

    # livros é uma lista de dicionarios,
    # cada dicionario tendo informacao de um livro

    for livro in livros:
        Livro.objects.create(
            titulo = livro['titulo'],
            autor = Autor.objects.get(nome = livro['autor']),
            genero = livro['genero'],
            ano_publicacao = livro['ano_publicacao']
            )