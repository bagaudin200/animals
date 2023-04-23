from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    arrival_date = models.DateField()
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    special_features = models.CharField(max_length=255)
