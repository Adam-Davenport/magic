from django.db import models
from sets.models import Set


# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    mtg_set = models.ForeignKey(Set)
    rarity = models.CharField(max_length=10)
    multiverse_id = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.name


class Battle(models.Model):
    set_name = models.CharField(max_length=3)
    date = models.DateField(auto_now_add=True, blank=True)


class Battle_Pack(models.Model):
    set_name = models.CharField(max_length=3)
    cards = models.FileField(upload_to='packs')
    battle = models.ForeignKey(Battle)
