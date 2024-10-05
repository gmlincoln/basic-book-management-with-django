from django.contrib import admin

from myApp.models import Book

# Register your models here.

@admin.register(Book)
class Book_Display(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'book_image', 'published_date')