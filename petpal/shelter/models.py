from django.db import models
from ..accounts.models import Shelter, User


class Pet(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    size = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.name


class Application(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    # Add more fields as needed
