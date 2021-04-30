import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import RenewBookForm

from catalog.models import BookInstance

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)

def renew_book_librarian(request,pk):
    book_instance = get_object_or_404(BookInstance,pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST' :
        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #you can use request.POST['renewal_date'] or request.GET['renewal_date'] but it's not recommended
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borroweds') )
    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form':form,
        'book_instance':book_instance
    }

    return render(request, 'catalog/book_renew_librarian.html',context)