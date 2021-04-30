from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy

from catalog.models import Book

class BookCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Book
    permission_required='catalog.can_mark_returned'
    fields = '__all__'


class BookUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Book
    permission_required='catalog.can_mark_returned'
    fields =  '__all__' # Not recommended (potential security issue if more fields added)



class BookDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Book
    permission_required='catalog.can_mark_returned' 
    success_url = reverse_lazy('books')

