from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg, Max, Min

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("rating")
    number_of_book = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, 'book_outlet/index.html', {'books': books, 'total_number_of_books': number_of_book, 'average_rating': avg_rating})

def book_detail(request, slug):
    # book = get_object_or_404(Book, pk=id)
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, "book_outlet/book_details.html", {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling,
    })