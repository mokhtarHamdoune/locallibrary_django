from django.views import generic
from catalog.models import Author

class AuthorListView (generic.ListView):
    model = Author