# pwsite/views.py

from django.shortcuts import render

def index_view(request):
    return render(request, "novoapp/index.html")

def document_view(request):
    return render(request, "novoapp/document.html")

def another_view(request):
    return render(request, "novoapp/another.html")