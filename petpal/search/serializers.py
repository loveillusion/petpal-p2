from rest_framework import serializers
from shelter.models import Pet


class PetSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['shelter', 'name', 'gender', 'breed', 'age', 'size', 'description', 'is_adopted']
