from django.db import models
from publishers.models import Publisher
from django.contrib.auth.models import User


class Platform(models.Model):
    name = models.CharField(max_length=20)
    releaseDate = models.DateField()
    publisher = models.ForeignKey(Publisher , on_delete=models.CASCADE)
    about = models.CharField(max_length=2000)
    picUrl = models.CharField(max_length=10)





class PlatformTrick(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    platform = models.ForeignKey(Platform,on_delete=models.CASCADE)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    createdAt = models.DateTimeField()