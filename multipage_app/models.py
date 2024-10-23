from django.db import models

class Page1(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name}'

class Page2(models.Model):
    author = models.ForeignKey(Page1, on_delete=models.CASCADE)




from django.db import models
# from .models import Book

class User(models.Model):
    # id_user = models.ForeignKey()
    time_entry = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.time_entry}'

class Product(models.Model):
    # id_product = models.ForeignKey(User, on_delete=models.CASCADE)
    name =  models.CharField(max_length=40)
    price = models.IntegerField()
    type_product = models.CharField(max_length=40)
    descriptions = models.CharField(max_length=100)


