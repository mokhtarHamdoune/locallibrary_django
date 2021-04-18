from django.views import generic
from catalog.models import Book

class BookDetailView(generic.DetailView):
    model = Book

    
    