from django.db import models
from shelter.models import Application
from django.conf import settings


class Chat(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
