from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
# from django.http import HttpResponse

# class Book:
#     def __init__(self,title,author,year):
#         self.title = title 
#         self.author = author
#         self.year = year

# books =[
#     Book('I Am Not Your Perfect Mexican Daughter' , 'Erika L. Sánchez', '2017'),
#     Book('Wash Day Diaries', 'Jamila R. & Robyn S.', '2022'),
# ]

# Create your views here.

def home(request): 
    # return HttpResponse('Hello World')
    return render(request, 'home.html')

def about(request): 
    # return HttpResponse('<h1>About My Book Collector </h1>')
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html',{'books':books})

def books_detail(request, book_id):
    book = Book.objects.get( id = book_id)
    return render(request, 'books/detail.html', {'book': book, })
    

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'books/book_form.html'
    success_url ='/books/'

class BookUpdate(UpdateView):
    model = Book 
    fields = '__all__'
    template_name = 'books/book_form.html'

class BookDelete(DeleteView):
    model = Book 
    success_url = '/books/'
    template_name = 'books/book_confirm_delete.html'

