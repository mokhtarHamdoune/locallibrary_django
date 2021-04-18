from django.views import generic 
from catalog.models import Author 

class AuthorDetailView(generic.DetailView):
    model = Author