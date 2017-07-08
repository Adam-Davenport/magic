from django.db import models


class Set(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=128)
    gatherer_code = models.CharField(max_length=128)
    release_date = models.DateField()