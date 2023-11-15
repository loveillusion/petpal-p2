from rest_framework import permissions
from shelter.models import Application


class IsShelterOrSeeker(permissions.BasePermission):
    """
    Custom permission to only allow the shelter owning the pet or the applicant of an application
    to view or comment on it.
    """

    def has_permission(self, request, view):
        application_id = view.kwargs['application_id']
        try:
            application = Application.objects.get(id=application_id)
        except Application.DoesNotExist:
            return False

        # Check if the request user is the shelter owner of the pet or the applicant
        shelter_user = application.pet.shelter.user
        applicant_user = application.applicant

        return request.user == shelter_user or request.user == applicant_user
