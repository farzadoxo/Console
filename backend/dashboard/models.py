from django.db import models
from games.models import Game
from django.contrib.auth.models import User
from tricks.models import Trick


class UserFavoritGame(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    game = models.ForeignKey(Game , on_delete=models.CASCADE)



class UserSavedTrick(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    trick = models.ForeignKey(Trick , on_delete=models.CASCADE)