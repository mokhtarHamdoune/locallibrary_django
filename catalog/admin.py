from django.contrib import admin
from .models import Author,Genre,BookInstance,Book,Language

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth','date_of_death')
    # with () will be horizontal layout like date_of_birth and date_of_death
    #in the fields is desiplayed if not then it's not displayed in the form
    fields = ['first_name','last_name',('date_of_birth', 'date_of_death')]
    #to exlude some attribute from the from (inputs)
    # exclude= ['first_name']
    # to add some more information the the author page 
    # here we will add book details in the bottom of the author details page
    inlines = [BookInline]

class BooksInstanceInline(admin.TabularInline):
    model=BookInstance
    # prevent to add more bookinstance 
    extra=0
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display__genre')
    inlines = [BooksInstanceInline]
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class  BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower','due_back','id')
    list_filter = ('status','due_back')
    fieldsets = (
        (None,{
        'fields':('book','imprint','id')
        }),('Availibility',{
            'fields':('status','due_back','borrower')
        }))
# Register your models here.    
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
# admin.site.register(Author)   
admin.site.register(Language)

# Register the admin class with the associated model
admin.site.register(Author,AuthorAdmin)