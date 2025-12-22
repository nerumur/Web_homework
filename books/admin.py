from django.contrib import admin
from books.models import *

admin.site.register(Books)
admin.site.register(UsersBooks)