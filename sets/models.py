from django.db import models


class Set(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=128)
    release_date = models.DateField()

    def __str__(self):
        return self.name
