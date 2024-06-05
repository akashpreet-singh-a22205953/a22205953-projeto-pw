import json
from .models import Artigos


with open('artigos/json/artigosdata.json') as f:
    data = json.load(f)
    for item in data:
        autor_name = item['autorName']
        post = item['post']
        comentario = item['comentario']
        rating = item['rating']
        Artigos.objects.create(autorName=autor_name, post=post, comentario=comentario, rating=rating)


