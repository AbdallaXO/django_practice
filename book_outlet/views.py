from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg


# Create your views here.
def index(request):
    books = Book.objects.all().order_by("rating")
    book_numbers = books.count()
    average = books.aggregate(Avg("rating"))
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "average": average,
            "book_numbers": book_numbers,
        },
    )


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "bestseller": book.is_bestselling,
        },
    )
