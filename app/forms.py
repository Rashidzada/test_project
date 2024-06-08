from .import models
from django import forms

from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input rounded-md shadow-sm border-gray-300'}),
            'email': forms.EmailInput(attrs={'class': 'form-input rounded-md shadow-sm border-gray-300'}),
            'subject': forms.TextInput(attrs={'class': 'form-input rounded-md shadow-sm border-gray-300'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea rounded-md shadow-sm border-gray-300'}),
        }


from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'author': forms.Select(attrs={'class': 'form-select'}),
        }


class CombinedForm(forms.Form):
    author = AuthorForm()
    book = BookForm()
