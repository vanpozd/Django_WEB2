from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import City  # Імпортуємо модель міста

class CustomUser(AbstractUser):
    cities = models.ManyToManyField(City, blank=True, related_name='users')
