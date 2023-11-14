from rest_framework import serializers
from .models import Chat
from shelter.models import Application


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['application', 'message', 'sender', 'timestamp']


class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['message']


class ApplicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['pet', 'applicant', 'app_status', 'app_message']


class ApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['app_status']
