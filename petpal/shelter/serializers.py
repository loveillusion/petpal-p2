from rest_framework import serializers
from .models import Pet, Application


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def create(self, validated_data):
        pet = Pet.objects.create_pet(**validated_data)
        return pet


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
