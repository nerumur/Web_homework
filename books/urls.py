from django.urls import path
from . import views

urlpatterns = [
    # Книги
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),

    # Выдачи книг
    path('userbooks/', views.UserBookListView.as_view(), name='userbook_list'),
    path('userbooks/<int:pk>/', views.UserBookDetailView.as_view(), name='userbook_detail'),
    path('userbooks/create/', views.UserBookCreateView.as_view(), name='userbook_create'),
    path('userbooks/<int:pk>/edit/', views.UserBookUpdateView.as_view(), name='userbook_update'),
    path('userbooks/<int:pk>/delete/', views.UserBookDeleteView.as_view(), name='userbook_delete'),
]