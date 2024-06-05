# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novoapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('document/', views.document_view, name='document'),
    path('another/', views.another_view, name='another'),
]