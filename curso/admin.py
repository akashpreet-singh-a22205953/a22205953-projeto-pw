from django.contrib import admin

from .models import Curso, area_Cientifica,disciplina,projeto,Docente,Linguagem_Programacao # Correct import

admin.site.register(Curso)
admin.site.register(area_Cientifica)
admin.site.register(disciplina)
admin.site.register(projeto)
admin.site.register(Docente)
admin.site.register(Linguagem_Programacao)




# Register your models here.
