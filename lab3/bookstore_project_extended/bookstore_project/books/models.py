from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_title_length(value):
    if not (10 <= len(value) <= 50):
        raise ValidationError('Title must be between 10 and 50 characters.')

def validate_category_name(value):
    if len(value) < 2:
        raise ValidationError('Category name must be at least 2 characters.')

class Category(models.Model):
    name = models.CharField(max_length=100, validators=[validate_category_name])

    def __str__(self):
        return self.name

class ISBN(models.Model):
    author_title = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.isbn_number

class Book(models.Model):
    title = models.CharField(max_length=200, validators=[validate_title_length])
    desc = models.TextField()
    rate = models.FloatField()
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
