from rest_framework import generics, permissions
from django.contrib.contenttypes.models import ContentType
from shelter.models import Shelter
from .models import Review
from .serializers import ReviewSerializer
from shelter.models import Application
from .pagination import CustomPagination
from .permissions import IsShelterOrSeeker


class ShelterReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        shelter_id = self.kwargs['shelter_id']
        shelter_type = ContentType.objects.get_for_model(Shelter)
        return Review.objects.filter(content_type=shelter_type, object_id=shelter_id)


class ShelterReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        shelter_id = self.kwargs['shelter_id']
        shelter_type = ContentType.objects.get_for_model(Shelter)
        serializer.save(author=self.request.user, content_type=shelter_type, object_id=shelter_id)


class ApplicationReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsShelterOrSeeker]
    pagination_class = CustomPagination

    def get_queryset(self):
        application_id = self.kwargs['application_id']
        application_type = ContentType.objects.get_for_model(Application)
        return Review.objects.filter(content_type=application_type, object_id=application_id)


class ApplicationReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsShelterOrSeeker]

    def perform_create(self, serializer):
        application_id = self.kwargs['application_id']
        application_type = ContentType.objects.get_for_model(Application)
        serializer.save(author=self.request.user, content_type=application_type, object_id=application_id)
