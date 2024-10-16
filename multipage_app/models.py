from django.db import models

class Page1(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name}'

class Page2(models.Model):
    author = models.ForeignKey(Page1, on_delete=models.CASCADE)
