from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from .models import Application
from accounts.models import Shelter


class ShelterCanViewSeekerProfile(BasePermission):
    message = "You do not have permission to view this applicant's profile."

    def has_permission(self, request, view):
        application_id = view.kwargs.get('application_id')
        shelter = request.user.shelter
        return Application.objects.filter(id=application_id, pet__shelter=shelter).exists()


class ShelterCanViewApplication(BasePermission):
    message = "You do not have permission to view these applications."

    def has_permission(self, request, view):
        shelter_id = view.kwargs.get('shelter_id')
        shelter = get_object_or_404(Shelter, id=shelter_id)
        return request.user.shelter == shelter
