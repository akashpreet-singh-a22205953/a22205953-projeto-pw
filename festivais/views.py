from django.shortcuts import render, get_object_or_404
from .models import Localizacao,Festival

def localizacao_list(request):
    localizacoes = Localizacao.objects.all()
    return render(request, 'festivais/localizacao_list.html', {'localizacoes': localizacoes})

def bandas_por_localizacao(request, localizacao_id):
    localizacao = get_object_or_404(Localizacao, pk=localizacao_id)
    return render(request, 'festivais/bandas_por_localizacao.html', {'localizacao': localizacao})



def bandas_por_festival(request, festival_id):
    festival = get_object_or_404(Festival, pk=festival_id)
    return render(request, 'festivais/bandas_por_festival.html', {'festival': festival})
