from catalog.models import BookInstance
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin
class AllBorrowedBooks(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    model = BookInstance
    permission_required='catalog.can_mark_returned'
    template_name =  'catalog/all_borrowed_books.html'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')
