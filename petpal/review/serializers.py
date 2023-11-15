from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'author', 'comment', 'created_at']
        read_only_fields = ['author', 'created_at']
