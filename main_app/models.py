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

class Reading(models.Model):
    TIMES = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening'),
    )
    date = models.DateField('reading date')
    time = models.CharField(max_length=1, choices=TIMES, default=TIMES[0][0], verbose_name = 'When')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def  __str__(self): 
        return f"{self.get_time_display()} on {self.date}"
    class Meta:
        ordering = '-date',