from rest_framework import generics, filters
from shelter.models import Pet
from shelter.serializers import PetSerializer


class PetSearchView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'gender', 'breed', 'age']
