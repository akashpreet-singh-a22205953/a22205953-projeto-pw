from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('<int:artigo_id>/', views.detail_view, name='detail_view'),
    path('criar/', views.criar_artigo, name='criar_artigo'),
    path('editar/<int:pk>/', views.editar_artigo, name='editar_artigo'),
    path('remover/<int:pk>/', views.remover_artigo, name='remover_artigo'),
]
