from django.db import models
from django.urls import reverse
class Author(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    date_of_birth= models.DateField(null=True,blank=True)

    date_of_death = models.DateField('Died',null=True,blank=True)

    class Meta:
        ordering =['last_name','first_name']
    
    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
