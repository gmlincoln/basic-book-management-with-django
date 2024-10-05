
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib import messages

from myApp.models import Book


def homePage(req):

    return render(req, 'index.html')


def addBook(req):

    if req.method == "POST":

        Book.objects.create(
            book_name = req.POST['book_name'],
            book_author = req.POST['book_author'],
            book_image = req.FILES['book_image'],
            published_date = req.POST['published_date']
        )
        messages.success(req,'Book added successfully!')    
        return redirect('viewBook')
    
    return render(req, 'add-book.html')

def viewBook(req):

    book_info = Book.objects.all()

    return render(req, 'view-book.html', {'books': book_info})


def singleView(req,book_id):

    #book_info = Book.objects.get(id=id)
    book_info = get_object_or_404(Book, id=book_id)

    context = {
        'book':book_info,
    }

    return render(req, 'single-view.html', context)

def deleteBook(req, book_id):

    book_info = Book.objects.filter(id=book_id)

    book_info.delete()

    return redirect('viewBook')


def editBook(req,book_id):

    book_info = get_object_or_404(Book, id=book_id)


    if req.method == 'POST':

        book_info.id = req.POST['book_id']

        book_info.book_name = req.POST['book_name']
        book_info.book_author = req.POST['book_author']
        
        if req.FILES.get('book_image'):
            book_info.book_image = req.FILES['book_image']

        book_info.published_date = req.POST['published_date']

        book_info.save()

        return redirect('viewBook')

    context = {
        'book':book_info
    }

    return render(req, 'edit-book.html', context)