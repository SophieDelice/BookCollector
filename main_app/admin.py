from django.contrib import admin

# Register your models here.
from .models import Book, Reading

admin.site.register(Book)
admin.site.register(Reading)
