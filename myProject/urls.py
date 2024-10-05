
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from myProject.views import addBook, homePage, singleView, viewBook



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('addBook/', addBook, name='addBook'),
    path('viewBook/', viewBook, name='viewBook'),
    path('singleView/', singleView, name='singleView'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
