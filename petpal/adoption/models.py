from django.db import models
from ..shelter.models import Application


class Chat(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
