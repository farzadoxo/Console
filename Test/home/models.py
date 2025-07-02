from django.db import models

# Create your models here.

class User(models.Model):
    FullName = models.CharField(max_length=15)
    Email = models.TextField()


class Book(models.Model):
    Title = models.CharField(max_length=30)
    Auther = models. CharField(max_length=20)



