from rest_framework import serializers

class NotificationCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    message = serializers.CharField()
    content_type = serializers.ChoiceField(choices=['chat', 'review', 'application'])
    object_id = serializers.IntegerField()
