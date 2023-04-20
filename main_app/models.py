from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse ('books_detail', kwargs={'book_id': self.id})

# class Category(models.Model):
#     genre = models.CharField(max_length=50)
