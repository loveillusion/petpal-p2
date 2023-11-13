from rest_framework import serializers
from .models import Chat
from shelter.models import Application


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['application', 'message', 'sender', 'timestamp']


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']
