from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=15)
    estabilishmenDate = models.DateField()
    logoUrl = models.CharField(max_length=100)