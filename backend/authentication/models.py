from django.db import models


class Platform(models.Model):
    Title = models.CharField(max_length=30)
    Company = models.CharField(max_length=10)
    ReleaseDate = models.DateTimeField()

class Game(models.Model):
    Title = models.CharField(max_length=50)
    Publisher = models.CharField(max_length=20)
    PublishDate = models.DateTimeField()
    Genre = models.CharField(max_length=10)
    ESRB = models.CharField(max_length=1)


