# urls.py
from django.urls import path
from . import views

app_name = 'festivais'
urlpatterns = [
    path('', views.localizacao_list, name='localizacao_list'),
    path('localizacao/<int:localizacao_id>/', views.bandas_por_localizacao, name='bandas_por_localizacao'),
    path('festival/<int:festival_id>/', views.bandas_por_festival, name='bandas_por_festival'),  
]
