from django.contrib import admin
from .models import Book, Author, Address

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating", "author")
    list_display = ("title", "author", "rating")
     
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)

    

# Register your models here.

