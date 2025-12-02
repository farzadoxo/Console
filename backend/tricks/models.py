from django.db import models
from games.models import Game
from django.contrib.auth.models import User


class Trick(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=5000)
    game = models.ForeignKey(Game , on_delete=models.CASCADE)
    creator = models.ForeignKey(User , on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)