from .models import Album, Banda, Musica
from django.shortcuts import render, redirect,get_object_or_404
from .forms import BandaForm,AlbumForm,MusicaForm


def editar_musica(request, pk):
    musica = get_object_or_404(Musica, pk=pk)
    if request.method == 'POST':
        # Handle form submission if needed
        return redirect('band:albuminfo_view')  # Redirect to the list of songs
    return render(request, 'Band/editar_musica.html', {'musica': musica})

def remover_musica(request, pk):
    musica = get_object_or_404(Musica, pk=pk)
    if request.method == 'POST':
        musica.delete()
        return redirect('band:albuminfo_view')  # Redirect to the list of songs
    return render(request, 'Band/remover_musica.html', {'musica': musica})

def editar_banda(request, pk):
    banda = get_object_or_404(Banda, pk=pk)
    if request.method == 'POST':
        form = BandaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('band:pagina_inicial')  # Redirect to the list of bands
    else:
        form = BandaForm(instance=banda)  # If you have a form for editing specific fields
    return render(request, 'Band/editar_banda.html', {'form': form})

def remover_banda(request, pk):
    banda = get_object_or_404(Banda, pk=pk)
    if request.method == 'POST':
        banda.delete()
        return redirect('band:pagina_inicial')  # Redirect to the list of bands
    return render(request, 'Band/pagina_inicial.html', {'banda': banda})


def editar_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('band:bandalbuns', banda_id=album.banda.id)  # Redirect to the list of albums for the band
    else:
        form = AlbumForm(instance=album)  # If you have a form for editing specific fields
    return render(request, 'Band/editar_album.html', {'form': form})

def remover_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('band:bandalbuns_view')  # Redirect to the list of albums
    return render(request, 'Band/remover_album.html', {'album': album})

def novo_Banda_view(request):
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nome_da_url_da_lista_de_bandas')  # Substitua 'nome_da_url_da_lista_de_bandas' pela URL real
    else:
        form = BandaForm()
    return render(request, 'Band/novoBanda.html', {'form': form})




def novo_album_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nome_da_url_da_lista_de_albuns')  # Substitua 'nome_da_url_da_lista_de_albuns' pela URL real
    else:
        form = AlbumForm()
    return render(request, 'Band/novo_album.html', {'form': form})

def nova_musica_view(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nome_da_url_da_lista_de_musicas')  # Substitua 'nome_da_url_da_lista_de_musicas' pela URL real
    else:
        form = MusicaForm()
    return render(request, 'Band/nova_musica.html', {'form': form})


def albuminfo_view(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {
        'album': album,
        'musicas': album.musicas.all(),
    }
    return render(request, "Band/albumInfo.html", context)

def pagina_inicial(request):
    bandas = Banda.objects.all().order_by('nome')
    context = {'bandas': bandas}
    return render(request, 'Band/paginaInicial.html', context)

def musicainfo_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    context = {'musica': musica}
    return render(request, 'Band/musicaInfo.html', context)


def bandalbuns_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    context = {
        'banda': banda,
        'albuns': banda.albuns.all(),
    }
    return render(request, "Band/bandaAlbuns.html", context)



