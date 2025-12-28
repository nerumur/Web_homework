from rest_framework import serializers
from django.contrib.auth.models import User
from books.models import Books, UsersBooks 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'genre_type', 'book_name', 'author', 'publication_date', 'publisher']

class UserBookInfoSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = UsersBooks
        fields = ['id', 'book', 'issue_date', 'return_date']

class UserSerializer(serializers.ModelSerializer):
    user_books = UserBookInfoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_books']