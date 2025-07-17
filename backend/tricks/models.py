from django.db import models
from games.models import Game
from django.contrib.auth.models import User


class Trick(models.Model):
    Title = models.CharField(max_length=40)
    Descreption = models.CharField(max_length=5000)
    Game = models.ForeignKey(Game , on_delete=models.CASCADE)
    Creator = models.ForeignKey(User , on_delete=models.CASCADE)