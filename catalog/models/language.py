from django.db import models

class Language(models.Model):

    name = models.CharField(max_length=100)

    book = models.ForeignKey('Book',on_delete=models.CASCADE)

    def __str__(self):
        return self.name