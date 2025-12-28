from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone
from books.models import Books, UsersBooks
from .serializers import BookSerializer, UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'], url_path='novelties')
    def novelties(self, request):
        """Возвращает книги, опубликованные в текущем году."""
        current_year = timezone.now().year
        books_this_year = Books.objects.filter(publication_date__year=current_year)
        serializer = self.get_serializer(books_this_year, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.prefetch_related('user_books__book')
    serializer_class = UserSerializer