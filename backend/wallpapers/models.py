from django.db import models
from games.models import Game
from platforms.models import Platform



class GameWallpaper(models.Model):
    game = models.ForeignKey(Game , on_delete=models.CASCADE)
    pic_url = models.CharField(max_length=60)




class PlatformWallpaper(models.Model):
    platform = models.ForeignKey(Platform,on_delete=models.CASCADE)
    pic_url = models.CharField(max_length=60)