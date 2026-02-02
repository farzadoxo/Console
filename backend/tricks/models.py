from django.db import models
from games.models import Game
from django.contrib.auth.models import User
from platforms.models import Platform


class GameTrick(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    game = models.ForeignKey(Game , on_delete=models.CASCADE)
    creator = models.ForeignKey(User , on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)




class PlatformTrick(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    platform = models.ForeignKey(Platform , on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)