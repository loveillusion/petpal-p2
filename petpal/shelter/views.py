from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Shelter, Pet, Application
from .serializers import PetSerializer, ApplicationSerializer
from accounts.serializers import ShelterSerializer
from rest_framework.response import Response


class ShelterDetailView(generics.RetrieveUpdateAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'shelter_id'


class ShelterListingsView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        shelter_id = self.kwargs.get('shelter_id')
        return Pet.objects.filter(shelter__id=shelter_id)


class ListAllSheltersView(generics.ListAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    permission_classes = [IsAuthenticated]


class CreatePetView(generics.CreateAPIView):
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        shelter_id = self.kwargs.get('shelter_id')
        shelter = Shelter.objects.get(id=shelter_id)
        serializer.save(shelter=shelter)


class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pet_id'

# Similarly, implement views for Update Pet and Adopt Pet
