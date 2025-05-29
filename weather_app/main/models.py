from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    temperature = models.CharField(max_length=10, blank=True)
    description = models.CharField(max_length=100, blank=True)
    humidity = models.CharField(max_length=10, blank=True)
    wind = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name
