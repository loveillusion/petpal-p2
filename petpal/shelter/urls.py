from django.urls import path
from .views import (
    ShelterDetailView,
    ShelterListingsView,
    ListAllSheltersView,
    CreatePetView,
    PetDetailView
)

urlpatterns = [
    path('shelter/<int:shelter_id>/', ShelterDetailView.as_view(), name='shelter_detail'),
    path('shelter/<int:shelter_id>/listings/', ShelterListingsView.as_view(), name='shelter_listings'),
    path('shelter/all/', ListAllSheltersView.as_view(), name='list_all_shelters'),
    path('shelter/<int:shelter_id>/pet/', CreatePetView.as_view(), name='create_pet'),
    path('shelter/<int:shelter_id>/pet/<int:pet_id>/detail/', PetDetailView.as_view(), name='pet_detail'),
]
