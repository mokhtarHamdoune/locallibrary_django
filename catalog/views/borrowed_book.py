from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from catalog.models import BookInstance
class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'

    def get_queryset(self):
         return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')