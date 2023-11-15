from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.pagination import PageNumberPagination

from .models import Chat, Application
from .serializers import ChatSerializer, ApplicationDetailSerializer, ApplicationUpdateSerializer, ChatCreateSerializer
from .permissions import ShelterCanViewSeekerProfile, ShelterCanViewApplication
from accounts.serializers import SeekerSerializer, UserSerializer
from accounts.models import Seeker
from rest_framework.response import Response


class ApplicationDetailView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'application_id'


class ChatView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        application_id = self.kwargs.get('application_id')
        return Chat.objects.filter(application__id=application_id)


class ChatCreateView(generics.CreateAPIView):
    serializer_class = ChatCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        application_id = self.kwargs.get('application_id')
        application = Application.objects.get(id=application_id)
        sender = self.request.user
        serializer.save(application=application, sender=sender)


class ApplicationStatusUpdateView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'application_id'

    def perform_update(self, serializer):
        serializer.save()


class ShelterViewSeekerProfile(generics.RetrieveAPIView):

        serializer_class = UserSerializer
        permission_classes = [permissions.IsAuthenticated, ShelterCanViewSeekerProfile]

        def retrieve(self, request, *args, **kwargs):
            application_id = self.kwargs.get('application_id')
            application = get_object_or_404(Application, id=application_id)
            applicant = application.applicant
            serializer = self.get_serializer(applicant)
            return Response(serializer.data)


class ApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ShelterCanViewApplication]

    def get_queryset(self):
        shelter_id = self.kwargs.get('shelter_id')
        status_filter = self.request.query_params.get('status', None)
        sort_by = self.request.query_params.get('sort_by', None)

        queryset = Application.objects.filter(pet__shelter__id=shelter_id)

        if status_filter:
            queryset = queryset.filter(app_status=status_filter)

        if sort_by == 'creation':
            queryset = queryset.order_by('created_at')
        elif sort_by == 'last_update':
            queryset = queryset.order_by('last_updated_at')

        return queryset

