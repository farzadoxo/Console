from django.db import models
from games.models import Game


class GameThemeSong(models.Model):
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    song_url = models.CharField(max_length=60)

