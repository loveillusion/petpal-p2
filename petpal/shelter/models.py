from django.db import models
from accounts.models import Shelter, User
from django.utils import timezone


class Pet(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, blank=True)
    breed = models.CharField(max_length=200, blank=True)
    age = models.PositiveIntegerField(null=True)
    size = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    is_adopted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Application(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    app_status = models.CharField(max_length=100)
    app_message = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    last_updated_at = models.DateTimeField(auto_now=True)
