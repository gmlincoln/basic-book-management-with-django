
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from myProject.views import addBook, deleteBook, editBook, homePage, singleView, viewBook



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('addBook/', addBook, name='addBook'),
    path('viewBook/', viewBook, name='viewBook'),
    path('singleView/<int:book_id>', singleView, name='singleView'),
    path('deleteBook/<int:book_id>', deleteBook, name='deleteBook'),
    path('editBook/<int:book_id>', editBook, name='editBook'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
