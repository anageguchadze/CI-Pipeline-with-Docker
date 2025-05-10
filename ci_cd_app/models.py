from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    habitat = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.species})"