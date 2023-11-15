from rest_framework.permissions import BasePermission
from .models import Application


class ShelterCanViewSeekerProfile(BasePermission):
    message = "You do not have permission to view this applicant's profile."

    def has_permission(self, request, view):
        application_id = view.kwargs.get('application_id')
        shelter = request.user.shelter
        return Application.objects.filter(id=application_id, pet__shelter=shelter).exists()

