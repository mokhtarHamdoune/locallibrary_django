from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
class Book(models.Model):
    # title fo the book
    title = models.CharField(max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)

    summary = models.TextField(max_length=1000,help_text='Enter a brief description of the book')

    isbn = models.CharField('ISBN',max_length=13,unique=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-dtails',args=[str(self.id)])

    def display__genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display__genre.short_description = 'Genre'

    