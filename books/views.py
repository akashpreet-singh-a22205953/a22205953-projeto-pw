from django.shortcuts import render
from .models import Book

# Create your views here.
def index_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/index.html', context)


def book_view(request, book_id):
    books = Book.objects.get(id = book_id)
    context={'books': books}
    return render(request,'books/book_detail.html',context)