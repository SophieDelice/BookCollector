from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField(default=0)


def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse ('books_detail', kwargs={'book_id': self.id})
