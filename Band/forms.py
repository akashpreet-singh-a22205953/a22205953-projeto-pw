# forms.py
from django import forms
from .models import Banda,Album,Musica

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nome', 'genero', 'foto']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'banda', 'lancamento', 'capa']




class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'album', 'duracao', 'link_spotify']