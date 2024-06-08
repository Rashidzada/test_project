from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=233)
    email = models.EmailField()
    subject = models.CharField(max_length=233)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
