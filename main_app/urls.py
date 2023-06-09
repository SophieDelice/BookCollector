from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='books_index'),
    path('books/<int:book_id>/', views.books_detail, name='books_detail'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'), 
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'), 
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'), 
    path('books/<int:book_id>/add_reading/', views.add_reading, name='add_reading'),
    path('accounts/signup/', views.signup, name='signup'),
]