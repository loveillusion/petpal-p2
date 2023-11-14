from django.urls import path
from .views import SeekerRegisterView, SeekerLoginView, SeekerProfileView, SeekerEditProfileView
from .views import ShelterRegisterView, ShelterLoginView, ShelterProfileView, ShelterEditProfileView


appname = 'accounts'
urlpatterns = [
    path('user/new/', SeekerRegisterView.as_view(), name='seeker_register'),
    path('user/login/', SeekerLoginView.as_view(), name='seeker_login'),
    path('user/profile/', SeekerProfileView.as_view(), name='seeker_profile'),
    path('user/profile/management/', SeekerEditProfileView.as_view(), name='seeker_edit_profile'),
    path('shelter/new/', ShelterRegisterView.as_view(), name='shelter_register'),
    path('shelter/login/', ShelterLoginView.as_view(), name='shelter_login'),
    path('shelter/profile/', ShelterProfileView.as_view(), name='shelter_profile'),
    path('shelter/profile/management/', ShelterEditProfileView.as_view(), name='shelter_edit_profile'),
]
