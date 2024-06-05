from django.contrib import admin

from .models import Autor, Livro  # Correct import

admin.site.register(Autor)
admin.site.register(Livro)

# Register your models here.
