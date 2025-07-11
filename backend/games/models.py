from django.db import models

class Game(models.Model):
    Title = models.CharField(max_length=20)
    Publisher = models.CharField(max_length=40)
    PublishDate = models.DateTimeField()
    Genere = models.CharField(max_length=10)
    ESRB = models.CharField(max_length=1)
    