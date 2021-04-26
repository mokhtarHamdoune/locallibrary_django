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
    # get the value of the 'num_visits' session key if does not exsit set it to 1
    num_visits = request.session.get('num_visits',1)
    # increment the session key 
    request.session['num_visits'] = num_visits + 1

    #if the key session is an object like a case then 
    # django with not recognize the changes if you made a change 
    # so you have to explicitly mark the session as having been modified.
    # Set session as modified to force data updates/cookie to be saved.
    
    # request.session.modified = True

    #context to send to the tamplate
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'hp_books': hp_books,
        'num_visits':num_visits
    }

    return render(request, 'index.html', context=context)
