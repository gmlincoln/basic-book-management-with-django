from django.db import models

# Create your models here.

class Book(models.Model):
    
    book_name = models.CharField(max_length=100, null=True)
    book_author = models.CharField(max_length=100, null=True)
    book_image = models.ImageField(upload_to='Media/Book_Image')
    published_date = models.DateField(max_length=20, null=True)

    def __str__(self):
        return f"{self.book_name}--{self.book_author}"