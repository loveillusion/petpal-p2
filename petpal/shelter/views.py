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


class UpdatePetView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pet_id'

    def perform_update(self, serializer):
        shelter_id = self.kwargs.get('shelter_id')
        shelter = Shelter.objects.get(id=shelter_id)
        serializer.save(shelter=shelter)


class AdoptPetView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pet_id = self.kwargs.get('pet_id')
        pet = Pet.objects.get(id=pet_id)

        # Check if pet is already adopted
        if pet.is_adopted:
            return Response({'detail': 'This pet has already been adopted.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        applicant = self.request.user
        app_status = 'Pending'

        serializer.save(pet=pet, applicant=applicant, app_status=app_status)

        # Update pet as adopted
        pet.is_adopted = True
        pet.save()

        return Response({'detail': 'Adoption application submitted successfully.'}, status=status.HTTP_201_CREATED)