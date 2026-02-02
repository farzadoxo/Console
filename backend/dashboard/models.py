from django.db import models
from games.models import Game
from django.contrib.auth.models import User
from tricks.models import GameTrick , PlatformTrick



class FavoritGame(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    game = models.ForeignKey(Game , on_delete=models.CASCADE)



class SavedGameTrick(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    trick = models.ForeignKey(GameTrick , on_delete=models.CASCADE)



class SavedPlatformTrick(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    trick = models.ForeignKey(PlatformTrick , on_delete=models.CASCADE)