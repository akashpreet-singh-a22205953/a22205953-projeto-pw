from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# noobsite/views.py


def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_view1(request):
    return HttpResponse("Bom dia, é meu primeiro site")

def index_view2(request):
    return HttpResponse("primeiro site sem utilzando wix😅")

def index_view3(request):
    return HttpResponse("HTML puro")
