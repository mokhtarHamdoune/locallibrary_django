from django.shortcuts import render
from catalog.models import Author, Book, BookInstance, Genre


def index(request):
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status='a').count() 

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    hp_books = Book.objects.filter(title__icontains='harry').count()

    #context to send to the tamplate
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'hp_books': hp_books
    }

    return render(request, 'index.html', context=context)
