from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def homePage(req):

    return render(req, 'index.html')


def addBook(req):
    
    return render(req, 'add-book.html')

def viewBook(req):

    return render(req, 'view-book.html')

def singleView(req):

    return render(req, 'single-view.html')