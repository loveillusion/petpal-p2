from django.urls import path
from .views import PetSearchView


appname = 'search'
urlpatterns = [
    path('', PetSearchView.as_view(), name='pet_search'),
]
