from rest_framework import generics, filters
from shelter.models import Pet
from .serializers import PetSearchSerializer


class PetSearchView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSearchSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['shelter__name', 'name', 'gender', 'breed', 'age', 'size', 'description', 'is_adopted']
    ordering_fields = ['name', 'age']
    # To sort by 'name' in ascending order: http://localhost:8000/search/?ordering=name
    # To sort by 'name' in descending order: http://localhost:8000/search/?ordering=-name
    # To sort by 'age' in ascending order: http://localhost:8000/search/?ordering=age
    # To sort by 'age' in descending order: http://localhost:8000/search/?ordering=-age
    ordering = ['name']  # default sorting
