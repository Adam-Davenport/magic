from django.db import models


# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    set = models.CharField(max_length=3)
    rarity = models.CharField(max_length=10)
