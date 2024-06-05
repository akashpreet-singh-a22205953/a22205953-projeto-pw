from django import forms
from .models import Artigos

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigos
        fields = ['autorName', 'post', 'comentario', 'rating']
