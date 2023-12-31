from rest_framework import serializers
from .models import Seeker, Shelter, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class SeekerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Seeker
        fields = ['user', 'first_name', 'last_name', 'contact_info', 'location', 'preferences', 'profile_picture']


class SeekerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeker
        fields = ['first_name', 'last_name', 'contact_info', 'location', 'preferences', 'profile_picture']


class ShelterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Shelter
        fields = ['user', 'name', 'contact_info', 'location', 'mission_statement', 'profile_picture']


class ShelterUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['name', 'contact_info', 'location', 'mission_statement', 'profile_picture']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)