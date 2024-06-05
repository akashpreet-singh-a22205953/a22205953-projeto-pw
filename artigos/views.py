from django.shortcuts import render,get_object_or_404,redirect
from .models import Artigos
from .forms import ArtigoForm


def index_view(request):
    context = {
        'artigos': Artigos.objects.all(),
    }
    return render(request, 'artigos/index.html', context)

def detail_view(request, artigo_id):
    artigo = get_object_or_404(Artigos, pk=artigo_id)
    return render(request, 'artigos/detail.html', {'artigo': artigo})




def criar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigos:index_view')  # Redirect to the index view
    else:
        form = ArtigoForm()
    return render(request, 'artigos/index.html', {'form': form})


def editar_artigo(request, pk):
    artigo = get_object_or_404(Artigos, pk=pk)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:index_view')
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/editar_artigo.html', {'form': form})

def remover_artigo(request, pk):
    artigo = get_object_or_404(Artigos, pk=pk)
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos:index_view')
    return redirect('artigos/index.html')  # Redirect in case of GET request