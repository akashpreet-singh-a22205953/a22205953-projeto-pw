# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name='noobsite'

urlpatterns = [
    path('index/', views.index_view),
    path('index1/', views.index_view1),
    path('index2/', views.index_view2),
    path('index3/', views.index_view3),
]