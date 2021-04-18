from django.views import generic
from catalog.models import Book

class BookListView(generic.ListView):
    model=Book
    paginate_by = 2
    # by default here will be book_list I just change to my_book_list
    # context_object_name = 'my_book_list'
    # queryset = Book.objects.filter(title__icontains='harry')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    # def get_queryset(self):
    #     return  Book.objects.filter(title__contains='war')[:5] # Get 5 books containing the title war

    # def get_context_data(self,**kwargs):
    #     # Call the base implementation first to get the context
    #     # get the existing context from our superclass.
    #     context = super(BookListView,self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context