# bandas/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'curso'
urlpatterns = [
  # ...
  path('', views.intro_view, name='intro_view'),
  path('curso/disciplinas/', views.todasDisciplinas_view, name='todasDisciplinas_view'),
  path('projetos/', views.projetos_view, name='projetos_view'),
  path('disciplina/<int:disciplina_id>/', views.disciplina_details, name='disciplina_details'),
  path('project/<int:project_id>/', views.project_details, name='project_details'),
#   path('editar/<int:pk>/', views.editar_disciplina, name='editar_disciplina'),
#   path('remover/<int:pk>/', views.remover_disciplina, name='remover_disciplina'),
  path('criar/', views.criar_disciplina, name='criar_disciplina'),
  path('criar/', views.criar_projeto, name='criar_projeto'),


  path('editar/disciplina/<int:pk>/', views.editar_disciplina, name='editar_disciplina'),
    path('remover/disciplina/<int:pk>/', views.remover_disciplina, name='remover_disciplina'),
    path('editar/projeto/<int:pk>/', views.editar_projeto, name='editar_projeto'),
    path('remover/projeto/<int:pk>/', views.remover_projeto, name='remover_projeto'),





]
