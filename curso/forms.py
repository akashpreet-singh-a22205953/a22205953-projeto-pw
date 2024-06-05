from django import forms
from .models import disciplina,projeto

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = disciplina
        fields = '__all__'




class ProjetoForm(forms.ModelForm):
    class Meta:
        model = projeto
        fields = '__all__'
