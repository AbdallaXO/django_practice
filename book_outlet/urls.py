from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="all-books"),
    path("<slug>", views.book_detail, name="book-detail")
]
