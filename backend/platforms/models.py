from django.db import models
from publishers.models import Publisher



class Platform(models.Model):
    name = models.CharField(max_length=20)
    releaseDate =models.DateField()
    publisher = models.ForeignKey(Publisher , on_delete=models.CASCADE)
    picUrl = models.CharField(max_length=10)
    about = models.CharField(max_length=2000)
