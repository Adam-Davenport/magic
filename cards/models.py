from django.db import models


# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    set = models.CharField(max_length=3)
    rarity = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Battle_Pack(models.Model):
    id = models.AutoField(primary_key=True)
    set_name = models.CharField(max_length=3)
    cards = models.FileField(upload_to='packs')
