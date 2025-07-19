from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=20)
    publisher = models.CharField(max_length=40)
    publishDate = models.DateField()
    genre = models.CharField(max_length=10)
    esrb = models.CharField(max_length=1)
    iconUrl = models.CharField(max_length=100)