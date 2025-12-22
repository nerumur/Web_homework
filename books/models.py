from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Классы, на основе которых создаются таблички в бд

class Books(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Художественная литература'),
        ('Science', 'Наука'),
        ('History', 'История'),
        ('Fantasy', 'Фантастика'),
        ('Mystery', 'Детектив'),
        ('Other', 'Прочее'),
    ]
    genre_type = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        default='Other', 
        verbose_name="Жанр"
    )
    book_name = models.CharField(
        max_length= 50,
        null=False,
        verbose_name= 'Название книги'
    )
    author = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Автор'
    )
    publication_date = models.DateField(
        null=False,
        verbose_name='Дата публикации'
    )
    publisher = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Издатель'
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['book_name']

    def __str__(self):
        return f"{self.book_name} by {self.author}"

class UsersBooks(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='user_books', 
        verbose_name="Пользователь"
        )
    book = models.ForeignKey(
        Books, 
        on_delete=models.CASCADE, 
        related_name='book_users', 
        verbose_name="Книга")
    issue_date = models.DateTimeField(
        default=timezone.now, 
        verbose_name="Дата выдачи"
        )
    return_date = models.DateTimeField(
        null=True, 
        blank=True, 
        verbose_name="Дата возврата"
        )
    class Meta:
        verbose_name = "Выданная книга"
        verbose_name_plural = "Выданные книги"
        ordering = ['-issue_date']

    def __str__(self):
        return f"{self.user.username} взял '{self.book.book_name}' ({self.issue_date.strftime('%Y-%m-%d')})"
