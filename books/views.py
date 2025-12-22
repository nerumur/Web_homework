from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Books, UsersBooks

# Books

class BookListView(ListView):
    model = Books
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Books
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Books
    template_name = 'books/book_form.html'
    fields = ['genre_type', 'book_name', 'author', 'publication_date', 'publisher']
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Books
    template_name = 'books/book_form.html'
    fields = ['genre_type', 'book_name', 'author', 'publication_date', 'publisher']
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

# UsersBooks

class UserBookListView(ListView):
    model = UsersBooks
    template_name = 'books/userbook_list.html'
    context_object_name = 'userbooks'

class UserBookDetailView(DetailView):
    model = UsersBooks
    template_name = 'books/userbook_detail.html'
    context_object_name = 'userbook'

class UserBookCreateView(CreateView):
    model = UsersBooks
    template_name = 'books/userbook_form.html'
    fields = ['user', 'book', 'issue_date', 'return_date']
    success_url = reverse_lazy('userbook_list')

class UserBookUpdateView(UpdateView):
    model = UsersBooks
    template_name = 'books/userbook_form.html'
    fields = ['user', 'book', 'issue_date', 'return_date']
    success_url = reverse_lazy('userbook_list')

class UserBookDeleteView(DeleteView):
    model = UsersBooks
    template_name = 'books/userbook_confirm_delete.html'
    success_url = reverse_lazy('userbook_list')

# from django.views.generic import TemplateView
