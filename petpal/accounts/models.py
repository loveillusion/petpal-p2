from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_seeker = models.BooleanField(default=False)
    is_shelter = models.BooleanField(default=False)


class Seeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    preferences = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.first_name


class Shelter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    mission_statement = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.name
