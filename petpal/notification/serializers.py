from rest_framework import serializers
from .models import Notification


class NotificationCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    message = serializers.CharField()
    content_type = serializers.ChoiceField(choices=['chat', 'review', 'application'])
    object_id = serializers.IntegerField()


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
