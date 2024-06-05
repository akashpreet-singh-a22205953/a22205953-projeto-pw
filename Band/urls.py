

from django.urls import path
from . import views

app_name = 'band'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('albuminfo/<int:album_id>/', views.albuminfo_view, name='albuminfo'),
    path('musicainfo/<int:musica_id>/', views.musicainfo_view, name='musicainfo'),
    path('bandalbuns/<int:banda_id>/', views.bandalbuns_view, name='bandalbuns'),
    path('novo-Banda/', views.novo_Banda_view, name='novo_Banda'),
    path('novo-album/', views.novo_album_view, name='novo_album_view'),
     path('nova-musica/', views.nova_musica_view, name='nova_musica_view'),
     path('editar_banda/<int:pk>/', views.editar_banda, name='editar_banda'),
    path('remover_banda/<int:pk>/', views.remover_banda, name='remover_banda'),
     path('editar_album/<int:pk>/', views.editar_album, name='editar_album'),
    path('remover_album/<int:pk>/', views.remover_album, name='remover_album'),
    path('editar_musica/<int:pk>/', views.editar_musica, name='editar_musica'),
    path('remover_musica/<int:pk>/', views.remover_musica, name='remover_musica'),


]