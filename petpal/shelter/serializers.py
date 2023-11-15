from rest_framework import serializers
from .models import Pet, Application


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['name', 'gender', 'breed', 'age', 'size', 'description', 'is_adopted']

    def create(self, validated_data):
        pet = Pet.objects.create(**validated_data)
        return pet


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['app_message']
