from django.shortcuts import render
from django.db import models
# from .models import Book

class Author(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}{self.surname}'

class Book(models.Model):
    name = models.CharField(max_length=40)
    year = models.IntegerField(max)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
