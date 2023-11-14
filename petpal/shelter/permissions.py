from rest_framework.permissions import BasePermission


class IsShelterUser(BasePermission):
    def has_permission(self, request, view):

        if request.user and request.user.is_authenticated:
            return request.user.is_shelter
        return False


class IsSeekerUser(BasePermission):
    def has_permission(self, request, view):

        if request.user and request.user.is_authenticated:
            return request.user.is_seeker
        return False
