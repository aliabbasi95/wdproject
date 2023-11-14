from django.http import HttpResponse
from django.template import loader

from product.models import Book, Category, Publisher


def books_view(request):
    books = Book.objects.all()
    content = {
        'books': books
    }
    templates = loader.get_template('product/books.html')
    return HttpResponse(templates.render(content, request))


def book_detail_view(request, pk):
    book = Book.objects.get(pk=pk)
    content = {
        'book': book
    }
    templates = loader.get_template('product/book_detail.html')
    return HttpResponse(templates.render(content, request))


def category_view(request, pk):
    category = Category.objects.get(pk=pk)
    content = {
        'category': category
    }
    templates = loader.get_template('product/category.html')
    return HttpResponse(templates.render(content, request))


def publisher_view(request, pk):
    publisher = Publisher.objects.get(pk=pk)
    print(publisher.books)
    content = {
        'publisher': publisher
    }
    templates = loader.get_template('product/publisher.html')
    return HttpResponse(templates.render(content, request))
