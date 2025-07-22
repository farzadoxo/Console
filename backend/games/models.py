from django.db import models



class Genre(models.Model):
    title = models.CharField(max_length=10)




class ESRB(models.Model):
    sign = models.CharField(max_length=1)
    ageRange = models.CharField(max_length=10)


    

class Publisher(models.Model):
    name = models.CharField(max_length=15)
    estabilishmenDate = models.DateField()
    logoUrl = models.CharField(max_length=100)





class Platform(models.Model):
    name = models.CharField(max_length=20)
    releaseDate =models.DateField()
    publisher = models.ForeignKey(Publisher , on_delete=models.CASCADE)
    picUrl = models.CharField(max_length=100)




class Game(models.Model):
    title = models.CharField(max_length=30)
    publisher = models.ForeignKey(Publisher , on_delete=models.CASCADE)
    publishDate = models.DateField()
    genre = models.ForeignKey(Genre , on_delete=models.CASCADE)
    esrb = models.ForeignKey(ESRB , on_delete=models.CASCADE)
    iconUrl = models.CharField(max_length=100)