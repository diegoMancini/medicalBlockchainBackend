from django.db import models

# Create your models here.


class Medicine(models.Model):

    name = models.CharField(max_length=20)
    envases = models.IntegerField()