from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('',views.index_view, name = 'index'),
    path('books/<int:book_id>/', views.book_view, name = 'book_view')
    ]