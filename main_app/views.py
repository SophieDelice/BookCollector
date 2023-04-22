from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Book
from .forms import ReadingForm
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

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

@login_required
def books_index(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/index.html',{'books':books})

@login_required
def books_detail(request, book_id):
    book = Book.objects.get( id = book_id)
    reading_form = ReadingForm()
    return render(request, 'books/detail.html', {
        'book': book, 
        'reading_form': reading_form 
    })

@login_required
def add_reading(request, book_id):
    form = ReadingForm(request.POST)
    print(form.errors)
    if form.is_valid():
        new_reading = form.save(commit=False)
        new_reading.book_id = book_id 
        new_reading.save()
    return redirect('books_detail', book_id=book_id)


def signup(request): 
    error_message =''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books_index')
        else: 
            print(form.errors)
            error_message = 'Invalid sign up - try again'
       
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form , 
        'error': error_message
    })

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ('title', 'author', 'year')
    template_name = 'books/book_form.html'
    success_url ='/books/'
    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookUpdate(UpdateView):
    model = Book 
    fields = '__all__'
    template_name = 'books/book_form.html'

class BookDelete(DeleteView):
    model = Book 
    success_url = '/books/'
    template_name = 'books/book_confirm_delete.html'

