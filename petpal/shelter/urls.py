from django.urls import path
from .views import (
    ShelterDetailView,
    ShelterListingsView,
    ListAllSheltersView,
    CreatePetView,
    PetDetailView,
    UpdatePetView,
    AdoptPetView
)

appname = 'shelter'

urlpatterns = [
    path('<int:shelter_id>/', ShelterDetailView.as_view(), name='shelter_detail'),
    path('<int:shelter_id>/listings/', ShelterListingsView.as_view(), name='shelter_listings'),
    path('all/', ListAllSheltersView.as_view(), name='list_all_shelters'),
    path('<int:shelter_id>/pet/', CreatePetView.as_view(), name='create_pet'),
    path('<int:shelter_id>/pet/<int:pet_id>/detail/', PetDetailView.as_view(), name='pet_detail'),
    path('<int:shelter_id>/pet/<int:pet_id>/management/', UpdatePetView.as_view(), name='update_pet'),
    path('<int:shelter_id>/pet/<int:pet_id>/adoption/', AdoptPetView.as_view(), name='adopt_pet'),
]
