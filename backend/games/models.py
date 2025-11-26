from django.db import models
from publishers.models import Publisher


class Genre(models.Model):
    title = models.CharField(max_length=10)




class ESRB(models.Model):
    sign = models.CharField(max_length=1)
    ageRange = models.CharField(max_length=10)



class Game(models.Model):
    title = models.CharField(max_length=30)
    publisher = models.ForeignKey(Publisher , on_delete=models.CASCADE)
    publishDate = models.DateField()
    genre = models.ForeignKey(Genre , on_delete=models.CASCADE)
    esrb = models.ForeignKey(ESRB , on_delete=models.CASCADE)
    iconUrl = models.CharField(max_length=100)
